from classes.float_math_class import float_math
from classes.float_pay_class import float_pay
from classes.float_operations_class import float_operations

math = float_math()
print(math.float_ave_height(50))
print(math.float_diameter(56.2))
print(math.float_diam_circum(45.67))
print(math.float_diam_area(38.5))
print(math.float_area_triangle(20.54,40.25))
print(math.float_height_triangle(32.2,63.25))
print(math.float_area_parallelogram(15.25,21.20))
print(math.float_height_parallelogram(13.25,14.56))

pay = float_pay([25.2,56.2],204.456,49.99,0.019,2.14)
print(pay.float_pay_money(45))
print(pay.float_money_convert(2000,"Usa"))
print(pay.float_verify())
print(pay.float_to_int())

operations = float_operations()
print(operations.float_add(4,5))
print(operations.float_sub(10,6))
print(operations.float_divide(10,5))
print(operations.float_mult(4,3))
print(operations.float_floor(10,2))
print(operations.float_exponent(10,2))
print(operations.float_modulo(20,4))

