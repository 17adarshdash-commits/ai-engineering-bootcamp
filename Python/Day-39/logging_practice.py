"""
logging_practice.py

Practice with the logging module: logging to both console and file,
demonstrating all five log levels, and logging an exception.
"""

import logging

LOG_FILE = "app.log"

logger = logging.getLogger("logging_practice")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def demonstrate_log_levels():
    """Log one message at each of the five standard log levels."""
    logger.debug("This is a DEBUG message - detailed diagnostic info.")
    logger.info("This is an INFO message - normal program event.")
    logger.warning("This is a WARNING message - something unexpected happened.")
    logger.error("This is an ERROR message - an operation failed.")
    logger.critical("This is a CRITICAL message - the program may not continue.")


def demonstrate_exception_logging():
    """Trigger an exception and log it with logging.exception()."""
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.exception("Caught an exception while dividing by zero.")


if __name__ == "__main__":
    logger.info("Starting logging_practice.py")

    print("=" * 50)
    print("Demonstrating all five log levels")
    print("=" * 50)
    demonstrate_log_levels()

    print()
    print("=" * 50)
    print("Demonstrating logging.exception() inside try/except")
    print("=" * 50)
    demonstrate_exception_logging()

    logger.info("Finished logging_practice.py")
    print(f"\nLogs were also written to '{LOG_FILE}'.")
