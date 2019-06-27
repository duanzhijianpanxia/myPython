# 利用logging的四大组件实现日志功能
# 打印出函数的执行时间，日志等级，日志消息
# 使用装饰器
# 不同的日志记录不同等级的日志
import logging

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)
# handler 处理器
# TimeRotationFileHandler是按照日期划分日志的
# RotationFileHandler 按照日志文件的大小划分日志

debug_handler = logging.FileHandler("1024debug1.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s"))

error_handler = logging.FileHandler("1024error1.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s"))

logger.addHandler(debug_handler)
logger.addHandler(error_handler)


def log(func):
    def wrapper(*arg, **kw):
        logger.debug("this is a debug message")
        logger.error("this is an error message")
        return func(*arg, **kw)

    return wrapper


def loghigher(text):
    def decorator(func):
        def wrapper(*arg, **kw):
            logger.debug(text)
            logger.error(text)
            return func(*arg, **kw)

        return wrapper

    return decorator


@log
def test():
    print("test done")


@loghigher("this is test1 done")
def test1():
    print("test1 done")


@loghigher("this is main done")
def main():
    print("main done")


test1()
main()