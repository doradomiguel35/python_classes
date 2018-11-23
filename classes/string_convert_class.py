class string_convert:
	def __init__(self,string):
		self.string = string

	def string_upper(self):
		string = str(self.string).upper()
		return string

	def string_lower(self):
		string = str(self.string).lower()
		return string

	def string_length(self):
		return len(self.string)

	def string_display(self):
		return str(self.string)

	def string_list(self):
		return list((self.string[slice(0,len(self.string))]))

	def string_tuple(self):
		return tuple((self.string[slice(0,len(self.string))]))

	def string_set(self):
		return set((self.string[slice(0,len(self.string))]))

	def string_int_str(self,num):
		num = str(num)
		return num

	def string_float_str(self,num):
		num = str(num)
		return str(type(num))


