class print_list:
	def __init__(self,array):
		self.array = array

	def list_loop(self):
		self.array =list(self.array)
		for x in self.array:
			print(x, end=" ")
		print()

	def list_while(self):
		self.array = list(self.array)
		x=0
		while x < len(self.array):
			print(self.array[x], end=", ")
			x+=1
		print()	

	def list_int(self):
		for x in self.array:
			x = int(x)
			print(x,end=", ")
		print()

	def list_float(self):
		for x in self.array:
			x = float(x)
			print(x,end=", ")
		print()

	def list_string(self):
		for x in self.array:
			x = str(x)
			print(x,end=", ")
		print()

	def list_bool(self):
		for x in self.array:
			if str(x) == "True" or str(x) == "False":
				print(x,end=" ")
			else:
				continue 
		print()
