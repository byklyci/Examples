

@classmethod
def foo(arg1,arg2):
    pass


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args , ** kwargs)
    return wrapper_func

class decorator_class(object):
    def __init__(self,original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)

@decorator_class
def display():
    print('display func ran ')

@decorator_func
def display_info(name,age):
    print('display info ran with arguments ({},{})'.format(name,age))

display_info('ali',20)
display()