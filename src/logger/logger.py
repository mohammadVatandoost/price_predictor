# from colorlog import ColoredFormatter
import colorlog
import logging


log_format = "%(asctime)s: %(message)s"
log_format2 = "%(asctime)s — %(levelname)s — %(name)s — %(message)s"


def init():
    # formatter = colorlog.ColoredFormatter(
    #     "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    #     datefmt=None,
    #     reset=True,
    #     log_colors={
    #         'DEBUG': 'cyan',
    #         'INFO': 'green',
    #         'WARNING': 'yellow',
    #         'ERROR': 'red',
    #         'CRITICAL': 'red,bg_white',
    #     },
    #     secondary_log_colors={},
    #     style='%'
    # )
    # colorlog.basicConfig(format=formatter)
    logging.basicConfig(format=log_format2, level=logging.DEBUG)
    return Log()


class Log:

    def get_scope(self, scope_name):
        logger = logging.getLogger(scope_name)
        logger.setLevel(logging.DEBUG)
        return logger




