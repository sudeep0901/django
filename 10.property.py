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