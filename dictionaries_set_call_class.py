from dictionaries_set_class import math_opt_dict
from dictionaries_set_class import dictionary_CRUD


operation = math_opt_dict({'num1': 1,'num2':3})
print(operation.dict_add_values())
print(operation.dict_sub_values())
print(operation.dict_multiply_values())
print(operation.dict_divide_values())

lists = {'first_name': 'Miguel',
		'last_name': 'Dorado',
		'home_town':'Davao City'}

crud = dictionary_CRUD('first_name','age',12,'home_town','Davao City','home_town',lists)
print(crud.dict_)


