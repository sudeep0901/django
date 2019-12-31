class ValuesClass(object):
    source = 'The class'

value_instance = ValuesClass()
print(value_instance.source)
print(value_instance.__class__)
print(value_instance.__class__.source)

 
def test(a, b, c, default=True, d=False, *e, **f):
    """ doc string """
    pass

import inspect
print(inspect.getargspec(test))
print(inspect.getdoc(test))


