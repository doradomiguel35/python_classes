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
	def __init__(self,search,
			key_add,key_add_value,
			key_update,key_update_value,
			key_remove,dictionary):
		self.search = search
		self.key_add = key_add
		self.key_add_value = key_add_value
		self.key_update = key_update
		self.key_update_value = key_update_value
		self.key_remove = key_remove
		self.dictionary = dictionary

	def dict_add(self):
		self.dictionary[self.key_add_value] = self.key_add_value
		return self.dictionary

	def dict_search(self):
		if self.search in self.dictionary:
			return str(self.dictionary[self.search])+" is present"
		else:
			return None

	def dict_update(self):
		self.dictionary[self.key_update] = self.key_update_value
		return self.dictionary

	def dict.remove(self):
		self.dictionary.pop(self.key_remove)
		return self.dictionary

# def dict_Assign(list1,list2):
# 	dictionary = dict() 

# 	for x in range(len(list1)):
# 		for y in range(len(list2)):
# 			dictionary[list1[x]] = list2[y]
# 			list2.pop(y)
# 			break

# 	return dictionary

# def dict_Concat_Value(dictionary,key1,key2):
# 	key1 = dictionary[key1]
# 	key2 = dictionary[key2]
# 	return str(key1)+" "+str(key2)

# def set_Add_Item(value1):
# 	sets = set((1,2,3,4,5))
# 	sets.add(value1)
# 	return sets

# def set_Get_Length(set):
# 	return len(set)

# def set_Remove_Item(set,item):
# 	set.remove(item)
# 	return set

# def set_Assign_To_Dict(set,item,value):
# 	dictionary = dict()
# 	if item in set:
# 		dictionary[item] = value
# 	return dictionary

# def set_Assign_To_List_of_Dict(set,item,value):
# 	lists = list(())
# 	dictionary = dict()
# 	if item in set:
# 		dictionary[item] = value
# 		lists.append(dictionary)
# 	return lists

# def set_Assign_To_Tuple(set,item,value):
# 	dictionary = dict()
# 	if item in set:
# 		dictionary[item] = value
# 		tuples = tuple((dictionary,1))
# 	return tuples

# def set_Length(set):
# 	return len(set)

# def set_Max_Value(set):
# 	return max(set)

# def set_Identify_Type(set,item):
# 	if item in set:
# 		return str(item)+" is "+str(type(item))
# 	else:
# 		return str("Item not Found")

# def set_Update_Items(set,item):
# 	set.update([item])
# 	return set
	
# print(dict_Add_Values(dict(a=1,b=2)))
# print(dict_Sub_Values(dict(a=4,b=5)))
# print(dict_Multiply_Values(dict(a=1,b=8)))
# print(dict_Divide_Values(dict(a=10,b=11)))
# print(dict_Search(dict(a=1,b=2),"a"))
# print(dict_Add(dict(a=10,b=11),"c",12))
# print(dict_Update(dict(a=10,b=11),"a",9))
# print(dict_Remove(dict(a=10,b=11,c=12),"c"))
# print(dict_Assign(list(("Miguel","Ghelo")),list((1,2))))
# print(dict_Concat_Value(dict(firstname="Miguel",lastname="Dorado"),"firstname","lastname"))
# print(set_Add_Item(6))
# print(set_Get_Length(set((1,2,3,4,5))))
# print(set_Remove_Item(set((1,23,4,5,6,)),23))
# print(set_Assign_To_Dict(set(("Banana","Apple","Carrot")),"Banana",1000))
# print(set_Assign_To_List_of_Dict(set(("Banana","Apple","Carrot")),"Banana",1000))
# print(set_Assign_To_Tuple(set(("Banana","Apple","Carrot")),"Banana",1000))
# print(set_Length(set(("Banana","Apple","Carrot"))))
# print(set_Max_Value(set(("Banana","Apple","Carrot"))))
# print(set_Identify_Type(set(("Banana","Apple","Carrot",1,1.5,True)),True))
# print(set_Update_Items(set(("Banana","Apple","Carrot",1,1.5,True)),"Pineapple"))