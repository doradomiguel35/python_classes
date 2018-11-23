import math
class float_math:
	def float_ave_height(self,maxHeight):
		aveHeight = (float(maxHeight)/2)
		return float(aveHeight)

	def float_diameter(self,radius):
		diameter = 2 * radius
		return float("%.2f" %diameter)

	def float_diam_circum(self,circumeference):
		diameter = circumeference/ math.pi
		return float("%.2f" %diameter)

	def float_diam_area(self,area):
		diameter = math.sqrt(area/math.pi) * 2
		return float("%.2f" %diameter)

	def float_area_triangle(self,base,height):
		area = 1/2 *(float(base) * float(height))
		return float("%.2f" %area)

	def float_height_triangle(self,area,base):
		height = (area/base) * 2
		return float("%.2f" %height)

	def float_area_parallelogram(self,base,height):
		area = base * height
		return float("%.2f" %area)

	def float_height_parallelogram(self,area,base):
		height = area/base
		return float("%.2f" %height)
