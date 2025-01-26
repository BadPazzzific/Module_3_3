def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c,)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['Владислав', 78, [1, 2, 3]]
values_dict = {'a' : [1, 2, 3], 'b' : 'Владислав', 'c' : 78}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'Владислав']
print_params(*values_list_2, 42)
