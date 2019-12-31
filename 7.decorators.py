
def decorate(func):
    print("Decorating the method %s" % func.__name__)

    def wrapper(*args, **kwargs):
        print("Args ", args)
        print("key Args ", kwargs)
        print("Called wrapped function with args:", args)
        return func(*args, **kwargs)
    print("Done")
    return wrapper


@decorate
def test(a, b):
    print("Added two numbers")
    return a + b


print(test(3, 14))


# Decorating with Extra Arguments

def decorator_args(func, prefix="Decorated"):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return "%s %s" % (prefix, func(*args, **kwargs))

    return wrapper


@decorator_args
def test(a, b, c):
    return a + b + c


print(test(10, 10, 30))


def decorator_args_new(prefix="Decorated"):
    def decorator(func):
        # print(globals())
        # print(locals())

        def wrapper(*args, **kwargs):
            return "%s %s" % (prefix, func(*args, **kwargs))
        return wrapper
    return decorator


@decorator_args_new(prefix="Custom")
def test1(a, b, c):
    return a + b + c


print(test1(30, 40, 50))


@decorator_args_new()
def test2(a, b, c):
    return a + b + c


print(test2(3, 88, 99))
