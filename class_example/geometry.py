class Square:
	def __init__(self, aa):
		self.a = aa

	def area(self):
		return self.a * self.a

	def perimeter(self):
		return self.a * 4


class Circle:
	def __init__(self, rr):
		self.r = rr

	def area(self):
		return self.r * self.r * 3.14159265

	def circumference(self):
		return self.r * 2 * 3.14159265
