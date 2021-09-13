# print((lambda x, y: x + y)(2, 3))
# z = lambda x, y: x + y
# print(z(2, 3))
#
# print((lambda x: x.upper())('bla bla bla'))
#

values = [1, 2, 3, 4, 5]
# def inc(value): return value + 10

# def my_map(func, args):
#     my_list = []
#     for i in args:
#         my_list.append(func(i))
#     return my_list
#
# def my_func(args):
#     args *= 3
#     return args
#
#
# print(my_map(my_func, values))
# print(my_map(lambda x: x*3, values))
#
# values = [1, 2, 3, 4, 5]
# print((lambda x: ''.join(str(s) for s in x))(values))

# my_str = 'KJjmklkmsfKLKJMfds'
# print(list(filter(lambda x: x.isupper(), my_str)))
#
#
# def my_filter(func, args):
#     my_list = []
#     for i in args:
#         if func(i):
#             my_list.append(i)
#     return my_list
#
#
# def my_func(args):
#     return args.isupper()
#
#
# print(my_filter(my_func, 'KJjmklkmsfKLKJMfds'))


# from functools import reduce
#
# print(reduce((lambda x, y: x ** y), [2, 2, 3, 4]))
# 
# subject_marks = [('Eanglish', 88), ('Science', 90)]
# print(subject_marks.sort(key=lambda x: x[1]))

# models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
# sorted_models = sorted(models, key=lambda x: x['color'])
# print(sorted_models)
# old_list = [1, 2, 3, 4, 7, 10]
# my_list = [el for el in old_list if el % 2 == 0]
# print(my_list)

# my_dict = {1: 2, 2: 3}
# dict_compr = {key:value for (value, key) in my_dict.items()}
# print(dict_compr)

def my_gen(huge_value):
    for x in range(huge_value):
        yield x

x = my_gen(100000)

print(x)


