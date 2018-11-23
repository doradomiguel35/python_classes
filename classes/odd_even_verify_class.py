class odd_even_verify:
	def __init__(self,num):
		self.num = num

	def bool_odd(self):
		if self.num % 2 != 0:
			return True
		else:
			return False

	def bool_even(self):
		if self.num % 2 == 0:
			return True
		else:
			return False
