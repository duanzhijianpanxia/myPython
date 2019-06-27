# 使用装饰器根据不同的函数，传入不同的日志
import logging

LOG_FORMAT = "%(asctime)s -- %(levelname)s -- %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
def log(text):
    def decorator(func):
        def wrapper(*arg,**kw):
            return func(*arg,**kw)
        return wrapper
    return decorator


@log("text done")
def test():
    print("test done")

@log("main done")
def main():
    print("main done")


test()
main()