class verify_data_type: 
	def __init__(
			self,lists,
			sets,dictionary,
			tuple):
		self.lists = lists
		self.sets = sets
		self.dictionary = dictionary
		self.tuple = tuple

	def bool_int(self,int):
		if str(type(int)) == "<class 'int'>":
			return True

		else:
			return False

	def bool_float(self,float):
		if str(type(float)) == "<class 'float'>":
			return True
		else:
			return False

	def bool_str(self,string):
		if str(type(string)) == "<class 'str'>":
			return True
		else:
			return False 

	def bool_boolean_verify(self,boolean):
		if str(type(boolean)) == "<class 'str'>":
			return False

		elif str(type(boolean)) == "<class 'bool'>":
			return True
		else:
			return False 

	def bool_list_verify(self):
		if str(type(self.lists)) == "<class 'list'>":
			return True
		else:
			return False 

	def bool_set_verify(self):
		if str(type(self.sets)) == "<class 'set'>":
			return True
		else:
			return False 

	def bool_tuple_verify(self):
		if str(type(self.tuple)) == "<class 'tuple'>":
			return True
		else:
			return False 


	def bool_dictionary_verify(self):
		if str(type(self.dictionary)) == "<class 'dict'>":
			return True
		else:
			return False 
