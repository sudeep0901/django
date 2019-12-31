import datetime


class CurrentDate(object):
    def __get__(self, instance, owner): 
        print(instance, owner)
        return datetime.date.today()

    def __set__(self, instance, value):
        raise NotImplementedError("Can't change Date")


class Example(object):
    date = CurrentDate()

e = Example()
print(e.date)



class Descriptor(object):
    def __init__(self, name):
        print("__init__ called")
        self.name = name
    
    def __get__(self, instance, owner):
        print("__get__ called")
        # return self.name
        print(instance)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("__set__ called")
        instance.__dict__[self.name] = value
        # self.name = value


class TestObject(object):
    attr = Descriptor("attr")
    attr1 = Descriptor("attr1")



test = TestObject()
test.attr = 6
test.attr1 = 61
print(test.attr, test.attr1)