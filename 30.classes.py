class SomeClassParent:
    def __init__(self, name='blabla'):
        self.name = name


class SomeClass(SomeClassParent):
    def __init__(self, param, name='f'):
        super(SomeClass, self).__init__(name)
        self.param = param

    def hop(self):
        print(self.name)

    def __repr__(self):
        return 'SomeClass(' + str(self.name) + ', ' + str(self.param) + ')'

    def __str__(self):
        return repr(self)

    def __lt__(self, other):
        return self.param < other.param

    def __gt__(self, other):
        return self.param > other.param

    def __le__(self, other):
        return self.param <= other.param

    def __ge__(self, other):
        return self.param >= other.param

    def __eq__(self, other):
        return self.param == other.param

    def __ne__(self, other):
        return self.param != other.param

    def __add__(self, other):
        return SomeClass(self.param + other.param)

    def __sub__(self, other):
        return SomeClass(self.param - other.param)

    def __isub__(self, other):
        return SomeClass(self.param - other.param)

    def __neg__(self):
        return SomeClass(-self.param)

    def __truediv__(self, other):
        return SomeClass(self.param/other.param)

    def __itruediv__(self, other):
        return SomeClass(self.param/other.param)

    def __mul__(self, other):
        return SomeClass(self.param * other.param)

    def __imul__(self, other):
        return SomeClass(self.param * other.param)

    def __floordiv__(self, other):
        return SomeClass(self.param//other.param)

    def __ifloordiv__(self, other):
        return SomeClass(self.param//other.param)

    def __mod__(self, other):
        return SomeClass(self.param % other.param)

    def __imod__(self, other):
        return SomeClass(self.param % other.param)

c = SomeClassParent('de')
b = SomeClass(88)
b.hop()
print(b)
print(str(b))
print(SomeClass(99) < b)