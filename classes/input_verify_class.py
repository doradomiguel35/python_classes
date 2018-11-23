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
