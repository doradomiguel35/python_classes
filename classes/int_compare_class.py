class int_compare:
	def int_greater_than(self,a,b):
		if a> b:
			return str(str(a)+" is greater than "+str(b))
		
		elif b > a:
			return str(str(b)+" is greater than "+str(a))

	def int_less_than(self,a,b):
		if a < b:
			return str(str(a)+" is less than"+str(b))
		elif b < a:
			return str(str(b)+" is less than"+str(a)) 

	def int_equal(self,a,b):
		if(a == b):
			return str(str(a)+" and "+str(b)+" are equal")

		else:
			return str("Both numbers are not equal")
