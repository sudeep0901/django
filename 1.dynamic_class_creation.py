"""
Like any Python object, a new type can be instantiated at any time, from any block of code. This means that your
code can construct a new class based on data collected at runtime. The following code demonstrates a way to declare
a class at runtime, which is functionally equivalent to the example provided in the previous section.
"""
DynamicClasses = type('DynamiClass', (), {'spam': 'eggs'})
print(DynamicClasses.spam)
DynamicClasses.test = 100
print(DynamicClasses.test)