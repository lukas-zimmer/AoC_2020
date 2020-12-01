import logging


class Logger:
    logger = logging.getLogger('aoc_logger')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('aoc_logs.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
