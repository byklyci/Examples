import time
import logging
from functools import wraps

def my_logger(original_func):
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args : {}, and kwargs {}'.format(args,kwargs))
        return original_func(*args, **kwargs)
    return wrapper

def timer(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args,**kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(original_func.__name__, t2))
        return result
    return wrapper

@my_logger
@timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with args {},{}'.format(name,age))

display_info('veli',35)


from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


@not_during_the_night
def say_whee():
    print("Whee!" + str(datetime.now().hour))

say_whee()


def makebold(func):
    @wraps(func)
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def makeitalic(func):
    @wraps(func)
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@makebold
@makeitalic

def printed():
    return 'this is the printed function'

print(printed())