class math_opt_dict:
	def __init__(self,dict):
		self.dict = dict

	def dict_add_values(self):
		result = 0
		for x in self.dict.values():
			result += x
		return result

	def dict_sub_values(self):
		result = max(self.dict.values())
		for x in self.dict.values():
			result -= x
		return result

	def dict_multiply_values(self):
		result = 1
		for x in self.dict.values():
			result *= x
		return result

	def dict_divide_values(self):
		result = 1
		for x in self.dict.values():
			result /= x
		return result
