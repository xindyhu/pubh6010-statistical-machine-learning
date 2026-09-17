# =============================================================================
# prepare_beach_ecoli.R
# Builds beach_ecoli.csv from the City of Chicago "Clear Water" repository
# (https://github.com/Chicago/e-coli-beach-predictions, MIT License).
#
# Students do NOT need to run this; beach_ecoli.csv is already provided.
# It is included so the dataset is fully reproducible.
#
# Design decisions (see README "Data notes"):
#   * Unit of analysis = one beach-day with a culture E. coli result.
#   * All weather / lake / lock predictors are PRIOR-DAY values. Samples are
#     collected in the morning, so same-day rain is not known at decision time
#     (using it would be information leakage).
#   * Prior-day E. coli is only filled when the previous sample at that beach
#     was exactly one calendar day earlier.
# =============================================================================

# Pin to a specific commit so the file never changes underneath us
commit <- "dd072196fea05163f643bae7612d19cb2ca7a40d"
url <- paste0("https://raw.githubusercontent.com/Chicago/e-coli-beach-predictions/",
              commit, "/Data/df.Rds")
raw_path <- file.path("raw", "clearwater_df.Rds")   # git-ignored (7.7 MB)
if (!file.exists(raw_path)) {
  dir.create(dirname(raw_path), showWarnings = FALSE, recursive = TRUE)
  download.file(url, raw_path, mode = "wb")
}
df <- readRDS(raw_path)

# Daily rainfall total (inches) = sum of 24 hourly precipitation intensities (in/hr).
# These hourly values come from the (discontinued) Dark Sky API, as redistributed in the
# City of Chicago repo. For fully public-domain weather, replace df$rain_in (and tmax /
# wind below) with NOAA GHCN-Daily values for Chicago O'Hare (station USW00094846;
# PRCP is in tenths of mm -> inches = PRCP / 254), merged on df$Date.
hourly <- paste0("precipIntensity_hourly_", 1:24)
df$rain_in <- rowSums(df[, hourly], na.rm = TRUE)
df$rain_in[rowSums(!is.na(df[, hourly])) == 0] <- NA
df$lock_open <- as.integer((df$Obrien.Lock.Open + df$CRCW.Lock.Open +
                            df$Wilmette.Lock.Open) > 0)

d <- df[, c("Client.ID", "Date", "Escherichia.coli", "rain_in", "temperatureMax",
            "windSpeed", "Water.Level", "lock_open")]
names(d) <- c("beach", "date", "ecoli", "rain_in", "tmax_f", "wind_mph",
              "lake_level_ft", "lock_open")
d$beach <- as.character(d$beach)
d <- d[order(d$beach, d$date), ]

# Lag helper: value from the previous row of the same beach, only if that row
# is exactly 1 day earlier
lag1 <- function(x, beach, date, k = 1) {
  n <- length(x)
  prev_same <- c(FALSE, beach[-1] == beach[-n])
  gap <- c(NA, as.numeric(diff(date)))
  out <- c(NA, x[-n])
  out[!prev_same | is.na(gap) | gap != 1] <- NA
  out
}
d$ecoli_lag1     <- lag1(d$ecoli, d$beach, d$date)
d$rain_lag1_in   <- lag1(d$rain_in, d$beach, d$date)
d$rain_lag2_in   <- lag1(d$rain_lag1_in, d$beach, d$date)
d$tmax_lag1_f    <- lag1(d$tmax_f, d$beach, d$date)
d$wind_lag1_mph  <- lag1(d$wind_mph, d$beach, d$date)
d$lake_lag1_ft   <- lag1(d$lake_level_ft, d$beach, d$date)
d$lock_open_lag1 <- lag1(d$lock_open, d$beach, d$date)

out <- data.frame(
  beach          = d$beach,
  date           = d$date,
  year           = as.integer(format(d$date, "%Y")),
  day_of_year    = as.integer(format(d$date, "%j")),
  ecoli          = d$ecoli,
  exceed         = as.integer(d$ecoli > 235),
  ecoli_cat      = cut(d$ecoli, c(-Inf, 126, 235, Inf),
                       labels = c("low", "moderate", "exceed")),
  ecoli_lag1     = d$ecoli_lag1,
  rain_lag1_in   = round(d$rain_lag1_in, 3),
  rain_48h_in    = round(d$rain_lag1_in + d$rain_lag2_in, 3),
  tmax_lag1_f    = d$tmax_lag1_f,
  wind_lag1_mph  = d$wind_lag1_mph,
  lake_lag1_ft   = d$lake_lag1_ft,
  lock_open_lag1 = d$lock_open_lag1
)
out <- out[complete.cases(out), ]
rownames(out) <- NULL

write.csv(out, "beach_ecoli.csv", row.names = FALSE)
cat("Wrote", nrow(out), "rows,", ncol(out), "columns\n")
cat("Exceedance prevalence:", round(mean(out$exceed), 3), "\n")
print(table(out$year))
