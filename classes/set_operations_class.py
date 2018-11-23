class set_operations:
	def __init__(self,set):
			self.set = set

	def set_add_item(self,item):
		self.set.add(item)
		return self.set

	def set_remove_item(self,item):
		self.set.remove(item)
		return self.set

	def set_get_length(self):
		return len(self.set)

	def set_max_value(self):
		try:
			return max(self.set)
		except:
			return str("Set should all have same datatype")

	def set_identify_type(self,item):
		if item in self.set:
			return str(item)+" is "+str(type(item))
		else:
			return str("Item not Found")
