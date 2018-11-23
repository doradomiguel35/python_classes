class int_print_loops:
	def int_for(self,a,b):
		for x in range(3,5):
			print(x, end=" ")
		print()

	def int_while(self,a,b):
		while a <= b:
			return a
			a+=1
		print()

	def int_recursion(self,a,b):
		while a <= b:
			return a
			a+=1
			return int_Recursion(a,b)
		

	def int_reverse(self,a,b):
		while b >= a:
			print(b,end=" ")
			b-=1
		print()

	def int_matrix(self,a,b):
		lineCount = 1
		for x in range(a):
			if lineCount != b:
				print(x+1,end=", ")
				lineCount+=1
			else:
				print(x+1,end=" ")
				print()
				lineCount=1
		print()

	def int_skip(self,a,b,c):
		for x in range(a,b,c):
			print(x,end=", ")
