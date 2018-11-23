class float_pay:
	def __init__(self,array,
			a,price,
			dollar,yen):
		self.array = array
		self.a = a
		self.price = price
		self.dollar = dollar
		self.yen = yen

	def float_pay_money(self,money):
		if float(money) >= float(self.price):
			change = float(money) - float(self.price)
			return str("Product Bought!")
			return str("Change: PHP %.2f" %change)
		else:
			return str("Isufficient funds")

	def float_money_convert(self,peso,countryAvailable):
		if str(countryAvailable.upper()) == "USA":
			money = peso * self.dollar
			return str("PHP -> USA = $ "+str(float(money)))

		elif str(countryAvailable.upper()) == "JAPAN":
			money = peso * self.yen
			return str("PHP -> JAPAN = YEN "+str(float(money)))

	def float_verify(self):
		for x in self.array:
			if str(type(x)) == "<class 'float'>":
				return str(str(x)+" is a float")

	def float_to_int(self):
		return int(self.a)
