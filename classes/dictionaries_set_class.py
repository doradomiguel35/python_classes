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

class dictionary_CRUD:
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