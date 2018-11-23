class list_crud:
	def __init__(self,array):
		self.array = array

	def list_add(self,addTo):
		self.array = list(self.array)
		self.array.append(addTo)
		return list(self.array)

	def list_remove(self,delete):
		self.array = list(self.array)
		self.array.remove(delete)
		return list(self.array)

	def list_insert(self,index,value):
		self.array = list(self.array)
		self.array.insert(index,value)
		return list(self.array)

	def list_pop(self):
		self.array = list(self.array)
		self.array.pop()
		return list(self.array)	