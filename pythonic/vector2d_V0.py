"""
doc test examples
>>> v1 = Vector2d(3, 4)
>>> print(v1.x, v1.y)
3.0 4.0
>>> x, y = v1
>>> x, y
(3.0, 4.0)
>>> v1
Vector2d(3.0, 4.0)
>>> v1_clone = eval(repr(v1))
>>> v1 == v1_clone
True
>>> print(v1)
(3.0, 4.0)
>>> octets = bytes(v1)
>>> octets
b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
>>> abs(v1)
5.0
>>> bool(v1), bool(Vector2d(0, 0))
(True, False)
>>> vc = Vector2d.from_bytes(octets)
>>> print(vc)
(3.0, 4.0)
>>> vc == v1
True
>>> vc is v1
False
>>> format(v1)
'(3.0, 4.0)'
>>> format(v1, '.4f')
'(3.0000, 4.0000)'
"""

from array import array
import math


class Vector2d:

    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        bytecode = chr(octets[0])
        mem = memoryview(octets[1:]).cast(bytecode)
        return cls(*mem)

    def __format__(self, format_spec=''):
        component = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*component)


