import logging
import os


def init_logging(log_dir):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s: %(message)s",  # format中必须包含message，否则不会记录
        datefmt="%m/%d/%Y %H:%M:%S %p",  # 对asctime进行format
        filename=os.path.join(log_dir, 'log.log')  # 日志记录在log.log，默认a模式
    )
    return logging.debug

