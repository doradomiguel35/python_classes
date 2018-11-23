from classes.int_collection_class import int_collection
from classes.int_compare_class import int_compare
from classes.int_operation_class import int_operation
from classes.int_print_loops_class import int_print_loops

collection = int_collection()
print(collection.int_list(4,5))
print(collection.int_tuples(4,5))
print(collection.int_set(4,5))
print(collection.int_dictionary(4,5))

compare = int_compare()
print(compare.int_greater_than(4,5))
print(compare.int_less_than(4,5))
print(compare.int_equal(5,5))

operation = int_operation()
print(operation.int_add(4,5))
print(operation.int_sub(4,5))
print(operation.int_multiply(4,5))
print(operation.int_divide(4,5))
print(operation.int_floor(4,5))
print(operation.int_exponent(4,5))
print(operation.int_modulo(4,5))

prints = int_print_loops()
print(prints.int_for(4,5))
print(prints.int_while(4,5))
print(prints.int_recursion(4,5))
print(prints.int_reverse(4,5))
print(prints.int_matrix(5,5))
print(prints.int_skip(2,20,2))




