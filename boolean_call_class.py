from boolean_class import boolean_compare
from boolean_class import verify_data_type
from boolean_class import list_pure_type
from boolean_class import odd_even_verify
from boolean_class import triangle_verify
from boolean_class import input_verify

compare = boolean_compare(12,4)
print(compare.bool_less())
print(compare.bool_greater())
print(compare.bool_equal())

verify = verify_data_type(5,'6',(7,8,9),{'index': 1},False)
print(verify.bool_int())
print(verify.bool_float())
print(verify.bool_str())
print(verify.bool_boolean_verify())
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
