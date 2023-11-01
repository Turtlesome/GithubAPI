import colorlog
import logging


formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s [%(name)s][%(levelname)s]%(reset)s %(message)s",
    datefmt="%Y%m%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
    reset=True,
)

# Create a StreamHandler that logs to the console
handler = colorlog.StreamHandler()
handler.setFormatter(formatter)


def setup_logger(filename=None):
    """
    Set up a logger with the specified name and sets its level to DEBUG with added handler to it.

    Arguments:
        name (str): The name of the logger.
        filename (str): The name of the file where logs will be written.

    Returns:
        log (logging.Logger): The newly created logger.
    """
    
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    if filename is not None:
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler) 

    return log