import time

def decorate(func):
    print("Decorting function %s" % func.__name__)
    def wrapped(*args, **kwargs):
        print("called wrapped function with arg:", args)
        return func(*args, **kwargs)
    print('done')
    return wrapped

def decorate(func, prefix="Decorated"):
    print("Decorting function %s" % func.__name__)
    def wrapped(*args, **kwargs):
        print("called wrapped function with arg :", args)
        return '%s: %s' % (prefix, func(*args, **kwargs))
    print('done')
    return wrapped


@decorate
def add(a, b):
    return a + b
# time.sleep(10000)
add(10,22)
# add = decorate(add)

simple = decorate(add)
custom = decorate(add, prefix="customer")

simple(10, 12)
custom(10, 12)

import functools

def add(a, b):
    return a + b

plus3 = functools.partial(add, 3)
plus5 = functools.partial(add, 5)

print(plus3(100))
print(plus5(1000))

