class dictionary_crud:
	def __init__(self,dictionary):
		self.dictionary = dictionary

	def dict_add(self,key_add,key_add_value):
		self.dictionary[key_add] = key_add_value
		return self.dictionary

	def dict_search(self,search):
		if search in self.dictionary:
			return str(self.dictionary[search])
		else:
			return None

	def dict_update(self,key_update,key_update_value):
		self.dictionary[key_update] = key_update_value
		return self.dictionary

	def dict_remove(self,key_remove):
		self.dictionary.pop(key_remove)
		return self.dictionary

	def dict_assign(self,list1,list2):
		for x in range(len(list1)):
			for y in range(len(list2)):
				self.dictionary[list1[x]] = list2[y]
				list2.pop(y)
				break

		return self.dictionary

	def dict_concat_value(self,key1,key2):
		key1 = self.dictionary[key1]
		key2 = self.dictionary[key2]
		return str(key1)+" "+str(key2)
