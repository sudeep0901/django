class CaseInsensitiveDict(dict):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self[key.lower()] = value

    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(key.lower())

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        return super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)


d = CaseInsensitiveDict(Spam='eggs')
print(d)
d['sPaM'] = 'burger'
print(d)
iter = iter(d)
print(next(iter))
# print(next(iter))


class Fibonacci(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        a, b = 0, 1
        for x in range(self.count):
            if x < 2:
                yield x
            else:
                c = a + b
                yield c
                a, b = b, c


for x in Fibonacci(5):
    print(x)


class FibonacciIterator(object):
    def __init__(self, count):
        self.a = 0
        self.b = 1
        self.count = count
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current > self.count:
            raise StopIteration
        if self.current < 3:
            return self.current - 1
            c = self.a + self.b
            self.a = self.b
            self.b = c
            return c
        next = __next__

    def __iter__(self):
        # Since it's already an iterator, this can return itself.
        return self


class Fibonacci(object):
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return FibonacciIterator(self.count)
