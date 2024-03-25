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
      "level": "DEBUG"
    },
    "error_file": {
      "class": "logging.FileHandler",
      "formatter": "default",
      "filename": "calc_error.log",
      "level": "ERROR"
    }
  },
  "root": {
    "handlers": ["console", "debug_file", "error_file"],
    "level": "DEBUG"
  }
}
