import logging, sys

from ocr_postproc import *
from my_ocr import *
from cq_med import settings

def log_handler():
    formatter = logging.Formatter('%(name)s [%(levelname)s]  %(asctime)s %(pathname)s - %(lineno)d: %(message)s')
    file_handler = logging.FileHandler(settings.LOG_FILE)
    file_handler.setFormatter(formatter)
    return file_handler

logger = logging.getLogger('cq-med')

logger.addHandler(log_handler())
logger.addHandler(logging.StreamHandler(sys.stderr))

logger.setLevel(logging.WARN)
