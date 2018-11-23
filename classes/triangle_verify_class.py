class triangle_verify:
	def __init__(self,opposite,
			adjacent,hypotenuse):
		self.opposite = opposite
		self.adjacent = adjacent
		self.hypotenuse = hypotenuse

	def bool_right_triangle(self):
		self.hypotenuse = self.hypotenuse **2
		legs = (self.opposite ** 2) + (self.adjacent ** 2)
		if legs == self.hypotenuse:
			return True
		else:
			return False
		
	def bool_acute_triangle(self):
		self.hypotenuse = self.hypotenuse **2
		legs = (self.opposite ** 2) + (self.adjacent ** 2)
		if legs > self.hypotenuse:
			return True
		else:
			return False

	def bool_obtuse_triangle(self):
		self.hypotenuse = self.hypotenuse **2
		legs = (self.opposite ** 2) + (self.adjacent ** 2)
		if legs < self.hypotenuse:
			return True
		else:
			return False
