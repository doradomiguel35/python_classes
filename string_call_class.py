from classes.string_manipulation_class import string_manipulation
from classes.identify_type_class import identify_type
from classes.string_convert_class import string_convert

manipulate = string_manipulation("I wanna fuck",['H','E','L','L','O'],('H','E','L','L','O'))
print(manipulate.string_profanity("fuck"))
print(manipulate.string_list_string())
print(manipulate.string_tuple_string())
print(manipulate.string_update("****","hug"))
print(manipulate.string_remove("hug"))

identify = identify_type()
print(identify.string_type_int(4))
print(identify.string_type_float(4.5))
print(identify.string_type_str('3'))
print(identify.string_type_bool('True'))
print(identify.string_type_list([1,'2','E']))
print(identify.string_type_set({"I","am","number","4"}))
print(identify.string_type_tuple((1,2,3,4,5)))

convert = string_convert("Hello")
print(convert.string_upper())
print(convert.string_lower())
print(convert.string_length())
print(convert.string_display())
print(convert.string_list())
print(convert.string_set())
print(convert.string_int_str(4))
print(convert.string_float_str(5.6))

