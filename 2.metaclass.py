"""
type is actually a metaclass—a class that creates other classes—and what we’ve been engaging in is called
metaprogramming. 2 In essence, metaprogramming creates or modifies code at runtime rather than at programming
time. Python allows you to customize this process by allowing a class to define a different metaclass to perform its work.
"""

class MetaClass(type):
    def __init__(cls, object_or_name, bases, attrs):
        print('Defining %s' % cls)
        print('Name %s' % object_or_name)
        print('Bases %s' % bases)
        print('Attributes:')
        attrs['addedinmeta'] = 'added in meta class'
        for (name,value) in attrs.items():
            print(name, value)


class RealClass(object, metaclass=MetaClass):
    spam = 'eggs'

RealClass

class SubClass(RealClass):
    # super()
    def foo(self):
        print("----------", self.spam)



class BaseAttribute(object):
    creation_counter = 1
    def __init__(self):
        self.creation_counter = BaseAttribute.creation_counter
        BaseAttribute.creation_counter += 1



class SubClassTracker(type):

    def __init__(cls, object_or_name, bases, dict):
        try:
            if TrackedClass not in bases:
                return
        except NameError:
            return
        TrackedClass._register.append(cls)

class TrackedClass(metaclass=SubClassTracker):
    _register = []

class ClassA(TrackedClass):
    pass

class ClassB(TrackedClass):
    pass

print(TrackedClass._register)