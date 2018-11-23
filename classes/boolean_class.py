class boolean_compare:
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2


	def bool_less(self):
		if self.num1 < self.num2:
			return True 
		else:
			return False

	def bool_greater(self):
		if self.num1 > self.num2:
			return True
		else:
			return False
		
	def bool_equal(self):
		if self.num1 == self.num2:
			return True
		else:
			return False


class verify_data_type: 
	def __init__(
			self,num,
			string,array,
			sets,boolean):
		self.num = num
		self.string = string
		self.array = array
		self.sets = sets
		self.boolean = boolean

	def bool_int(self):
		if str(type(self.num)) == "<class 'int'>":
			return True

		else:
			return False

	def bool_float(self):
		if str(type(self.num)) == "<class 'float'>":
			return True
		else:
			return False

	def bool_str(self):
		if str(type(self.string)) == "<class 'str'>":
			return True
		else:
			return False 

	def bool_boolean_verify(self):
		if str(type(self.boolean)) == "<class 'str'>":
			return False

		elif str(type(self.boolean)) == "<class 'bool'>":
			return True
		else:
			return False 

	def bool_list_verify(self):
		if str(type(self.array)) == "<class 'list'>":
			return True
		else:
			return False 

	def bool_set_verify(self):
		if str(type(self.sets)) == "<class 'set'>":
			return True
		else:
			return False 

	def bool_tuple_verify(self):
		if str(type(self.array)) == "<class 'tuple'>":
			return True
		else:
			return False 


	def bool_dictionary_verify(self):
		if str(type(self.sets)) == "<class 'dict'>":
			return True
		else:
			return False 

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

class odd_even_verify:
	def __init__(self,num):
		self.num = num

	def bool_odd(self):
		if self.num % 2 != 0:
			return True
		else:
			return False

	def bool_even(self):
		if self.num % 2 == 0:
			return True
		else:
			return False

class triangle_verify:
	def __init__(self,opposite,
			adjacent,hypotenuse):
		self.opposite = opposite
		self.adjacent = adjacent
		self.hypotenuse = hypotenuse

	def bool_right_triangle(self):
		self.hypotenuse = self.hypotenuse **2
		legs = (self.opposite ** 2) + (self.adjacent ** 2)
		if legs == self.hypotenuse:
			return True
		else:
			return False
		
	def bool_acute_triangle(self):
		self.hypotenuse = self.hypotenuse **2
		legs = (self.opposite ** 2) + (self.adjacent ** 2)
		if legs > self.hypotenuse:
			return True
		else:
			return False

	def bool_obtuse_triangle(self):
		self.hypotenuse = self.hypotenuse **2
		legs = (self.opposite ** 2) + (self.adjacent ** 2)
		if legs < self.hypotenuse:
			return True
		else:
			return False


class input_verify:
	def __init__(self,email):
		self.email = email

	def bool_email_verify(self):

		if str(".com") in self.email and str("@gmail") in self.email and str("@yahoo.com"):
			if str(" ") in self.email:
				return False
			else:
				return True
		else:
			return False
