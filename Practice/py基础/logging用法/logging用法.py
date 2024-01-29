import logging

"""
在 Python 的 logging 模块中，有以下几个标准的日志级别，按照严重性递增：
DEBUG：最详细的日志级别，主要用于调试和详细信息记录。
INFO：提供程序的一般信息，表示程序正在正常工作。
WARNING：表示发生了一些可能是错误的情况，但程序仍然可以正常运行。
ERROR：指示发生了一个错误，程序可能无法正常执行某些功能。
CRITICAL：表示严重错误，可能导致程序终止执行。
设置INFO后 只会输出INFO及以后的消息
"""


# 配置基本的日志设置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')  # 自定义时间格式


def example_function():
    # 在函数中记录日志
    logging.info('这是来自示例函数的 INFO 消息。')
    logging.warning('这是来自示例函数的 WARNING 消息。')


if __name__ == "__main__":
    # 记录不同级别的日志
    logging.debug('This is a DEBUG message.')
    logging.info('This is an INFO message.')
    logging.warning('This is a WARNING message.')
    logging.error('This is an ERROR message.')
    logging.critical('This is a CRITICAL message.')

    # 调用函数，产生函数内的日志
    example_function()
