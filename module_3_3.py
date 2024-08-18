def print_params(a=1, b="Строка", c=True):
    print(a, b, c)
    print()


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [2, "Столбец", False]
value_list_1 = [True, "Thomas"]
value_dict = {"c": 32}
print_params(*value_list_1, **value_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
