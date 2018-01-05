#!/usr/bin/python

from geometry import Square, Circle

a = Square(5)
b = Square(10)

c = Circle(7)

print "Area of a is", a.area()
print "Area of b is", b.area()
print "Area of c is", c.area()

print "Perimeter of a is %s" % (a.perimeter())
print "Perimeter of b is %s" % (b.perimeter())
print "Circumference of c is %s" % (c.circumference())
