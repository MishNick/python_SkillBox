dict_config = {
  "version": 1,
  "formatters": {
    "default": {
      "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
    }
  },
  "handlers": {
    "console": {
      "class": "logging.StreamHandler",
      "formatter": "default",
      "level": "INFO"
    },
    "debug_file": {
      "class": "logging.FileHandler",
      "formatter": "default",
      "filename": "calc_debug.log",
      "level": "DEBUG",
      "filters": ["ascii_filter"]
    },
    "error_file": {
      "class": "logging.FileHandler",
      "formatter": "default",
      "filename": "calc_error.log",
      "level": "ERROR",
      "filters": ["ascii_filter"]
    },
    "utils_file": {
      "class": "logging.handlers.TimedRotatingFileHandler",
      "formatter": "default",
      "filename": "utils.log",
      "when": "H",
      "interval": 1,
      "backupCount": 6,
      "level": "INFO",
      "filters": ["ascii_filter"]
    }
  },
  "filters": {
    "ascii_filter": {
      "()": "utils.ASCIIFilter"
    }
  },
  "root": {
    "handlers": ["console", "debug_file", "error_file", "utils_file"],
    "level": "DEBUG"
  }
}

