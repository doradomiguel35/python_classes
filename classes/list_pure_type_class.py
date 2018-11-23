class list_pure_type:
	def __init__(self,lists):
		self.lists = lists

	def bool_int_list(self):
		result = True
		for x in self.lists:
			if type(x) != type(int()):
				result = False
				break
		return result

	def bool_float_list(self):
		result = True
		for x in self.lists:
			if type(x) != type(float()):
				result = False
				break
		return result

	def bool_str_list(self):
		result = True
		for x in self.lists:
			if type(x) != type(str()):
				result = False
				break
		return result
