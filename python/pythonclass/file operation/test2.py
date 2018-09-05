import test
print test.add(10,20)
print test.power(10,2)
print test.mul(10,5)
from test import add
print add(10,20)
from test import add, mul
print mul(10,2)
from test import *
print power(10,2)