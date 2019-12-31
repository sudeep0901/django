def accept(**kwargs):
    for keyword, value in kwargs.items():
        print("%s -> %r" % (keyword, value))

accept(name="sudeep", lastName="patel")
    

# Required arguments
# • Optional arguments
# • Excess positional arguments
# • Excess keyword arguments
# def complex_function(a, b=None, *c, **d):



# >>> add(a=7, *args)
# Traceback (most recent call last):
# ...
# TypeError: add() got multiple values for keyword argument 'a'
# >>> add(1, 2, a=7)
# Traceback (most recent call last):
# ...
# TypeError: add() got multiple values for keyword argument 'a'