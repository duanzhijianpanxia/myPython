import logging

LOG_FORMAT=("%(asctime)s -- %(levelname)s -- %(message)s")
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

def log(func):
    def wrapper(*arg,**kw):
        logging.error("this is an error")
        return func(*arg, **kw)
    return wrapper

@log
def test():
    print("test done")

test()