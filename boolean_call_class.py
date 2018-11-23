from classes.boolean_compare_class import boolean_compare
from classes.verify_data_type_class import verify_data_type   
from classes.list_pure_type_class import list_pure_type
from classes.odd_even_verify_class import odd_even_verify
from classes.triangle_verify_class import triangle_verify
from classes.input_verify_class import input_verify

compare = boolean_compare()
print(compare.bool_less(12,4))
print(compare.bool_greater(12,4))
print(compare.bool_equal(12,4))

verify = verify_data_type([12,4],{4,5},{'int': 4},(5,6))
print(verify.bool_int(4))
print(verify.bool_float(4.6))
print(verify.bool_str("Hi"))
print(verify.bool_boolean_verify(False))
print(verify.bool_list_verify())
print(verify.bool_set_verify())
print(verify.bool_tuple_verify())
print(verify.bool_dictionary_verify())

pure_list = list_pure_type([1,2,3,4,5])
print(pure_list.bool_int_list())
print(pure_list.bool_float_list())
print(pure_list.bool_str_list())

odd_even = odd_even_verify(4)
print(odd_even.bool_odd())
print(odd_even.bool_even())

triangle_verify = triangle_verify(4,5,7)
print(triangle_verify.bool_right_triangle())
print(triangle_verify.bool_acute_triangle())
print(triangle_verify.bool_obtuse_triangle())

input_verify = input_verify("doradomiguel35@gmail.com")
print(input_verify.bool_email_verify())
