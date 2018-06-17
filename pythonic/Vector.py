"""
>>> v1 = Vector([3,4,5])
>>> len(v1)
3
>>> v1[0], v1[-1]
(3.0, 5.0)
>>> v7 = Vector(range(7))
>>> v7[1:4]
Vector[[1.0, 2.0, 3.0]]
>>> v7[-1:]
Vector[[6.0]]
>>> v7[1,2]
Traceback (most recent call last):
    ...
TypeError: Vector indices must be integers

>>> v= Vector(range(5))
>>> v
Vector[[0.0, 1.0, 2.0, 3.0, 4.0]]
>>> v.x
0.0
>>> v.x = 10
Traceback (most recent call last):
    ...
AttributeError: readonly attribute 'x'
>>> v
Vector[[0.0, 1.0, 2.0, 3.0, 4.0]]
>>> vv =Vector([0.0, 1.0, 2.0, 3.0, 4.0])
>>> v == vv
True
"""

from array import array
import functools
import operator
import reprlib
import math
import numbers

class Vector(object):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector[{}]'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(other) == tuple(self)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return abs(self) != 0

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:])
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __hash__(self):
        hashs = map(hash, self._components)
        return functools.reduce(operator.xor, hashs, 0)