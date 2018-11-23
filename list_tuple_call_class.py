from classes.tuple_count_odd_even_class import tuple_count_odd_even
from classes.print_list_class import print_list
from classes.list_crud_class import list_crud 

op_odd_even = tuple_count_odd_even((1,2,3,4,5,6,7,8,9,))
print(op_odd_even.tuple_add_odd())
print(op_odd_even.tuple_add_even())
print(op_odd_even.tuple_multiply_odd())
print(op_odd_even.tuple_multiply_even())
print(op_odd_even.tuple_count(1))
print(op_odd_even.tuple_index(5))

prints = print_list([1,2,3,4,5,6,7,8,9,])
print(prints.list_loop())
print(prints.list_while())
print(prints.list_int())
print(prints.list_float())
print(prints.list_string())
print(prints.list_bool())

crud = list_crud([1,2,3,4,5,6])
print(crud.list_add(7))
print(crud.list_remove(6))
print(crud.list_insert(4,8))
print(crud.list_pop())
