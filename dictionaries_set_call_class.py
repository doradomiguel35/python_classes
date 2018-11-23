from classes.math_opt_dict_class import math_opt_dict
from classes.dictionary_crud_class import dictionary_crud
from classes.set_operations_class import set_operations
from classes.set_assign_class import set_assign

crud_dict = {'first_name': 'Miguel',
			'last_name': 'Dorado',
			'home_town':'Davao City'}

sets = {"banana","apple","pineapple","strawberry",35,25,45,140}

operation = math_opt_dict({'num1': 56,'num2':2})
print(operation.dict_add_values())
print(operation.dict_sub_values())
print(operation.dict_multiply_values())
print(operation.dict_divide_values())

crud = dictionary_crud(crud_dict)
print(crud.dict_add('age',12,))
print(crud.dict_search('first_name'))
print(crud.dict_update('home_town','Manila City'))
print(crud.dict_remove('home_town'))
print(crud.dict_assign(['mother','father'],['Arlyn Dorado','Castor Dorado']))
print(crud.dict_concat_value('first_name','last_name'))

set_op = set_operations(sets)
print(set_op.set_add_item('raspberry'))
print(set_op.set_remove_item('banana'))
print(set_op.set_get_length())
print(set_op.set_max_value())
print(set_op.set_identify_type('strawberry'))

set_assign = set_assign(sets)
print(set_assign.set_assign_to_dict('apple',25))
print(set_assign.set_assign_to_list_of_dict('strawberry',140))
print(set_assign.set_assign_to_tuple_of_dict('pineapple',45))
