class PropClass:

    def __init__(self, name=""):
        self._name = name

    @property
    def name(self):
        return self._name

    def get_name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

    name_prop = property(get_name)

pclass = PropClass()

dir(pclass)

pclass.name = "Sudeep Patel"
print(pclass.name)
print(pclass.name_prop)


class Person:
    name = "sudeep"
    age = 34

person  = Person()
print(getattr(person, "name1", "Namasvi"))
setattr(person, "name", "Manasvi")
print(person.name)