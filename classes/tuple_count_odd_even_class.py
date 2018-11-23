class tuple_count_odd_even:
	def __init__(self,tuple):
		self.tuple = tuple

	def tuple_add_odd(self):
		result = 0
		for x in self.tuple:
			if x % 2 != 0:
				result+=x
		return result

	def tuple_add_even(self):
		result = 0
		for x in self.tuple:
			if x % 2 == 0:
				result+=x
		return result

	def tuple_multiply_odd(self):
		result = 1
		for x in self.tuple:
			if x % 2 != 0:
				result*=x
		return result

	def tuple_multiply_even(self):
		result = 1
		for x in self.tuple:
			if x % 2 == 0:
				result*=x
		return result

	def tuple_count(self,num):
			return str(self.tuple.count(num))


	def tuple_index(self,num):
		return str(self.tuple.index(num))
