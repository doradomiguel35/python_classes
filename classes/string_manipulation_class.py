class string_manipulation:
	def __init__(self,string,
			list,tuple):
		self.string = string
		self.list = list
		self.tuple = tuple

	def string_profanity(self,filters):
		if filters in self.string:
			self.string = self.string.replace(filters, "****")
		return str(self.string)

	def string_list_string(self):
		try:
			string = str()
			for x in self.list:
				string+=x
			return string
		except:
			return str("List should all be type 'str'")

	def string_tuple_string(self):
		try:
			string = str()
			for x in self.tuple:
				string+=x
			return string
		except:
			return str("Tuple should all be type 'str'")

	def string_remove(self,remove):
		if remove in self.string:
			self.string = self.string.replace(remove, "")
		return str(self.string)

	def string_update(self,update,replace):
		if update in self.string:
			self.string = self.string.replace(update, replace)
		return str(self.string)
