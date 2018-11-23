class int_collection:
	def int_list(self,a,b):
		result = list((a,b))
		return result

	def int_tuples(self,a,b):
		result = tuple((a,b))
		return result

	def int_set(self,a,b):
		result = set((a,b))
		return result

	def int_dictionary(self,a,b):
		result = {'num1': a,'num2': b}
		return result
