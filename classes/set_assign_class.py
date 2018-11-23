class set_assign:
	def __init__(self,set):
		self.set = set

	def set_assign_to_dict(self,item,value):
		dictionary = dict()
		if item in self.set:
			dictionary[item] = value
		return dictionary

	def set_assign_to_list_of_dict(self,item,value):
		lists = list(())
		dictionary = dict()
		if item in self.set:
			dictionary[item] = value
			lists.append(dictionary)
		return lists

	def set_assign_to_tuple_of_dict(self,item,value):
		dictionary = dict()
		if item in self.set:
			dictionary[item] = value
			tuples = tuple((dictionary,))
		return tuples