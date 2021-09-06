# def my_function(x, y, *fff):
#     print(fff)
#     if x == 0:
#         return 'Wrong'
#     return x + y
#
# print(my_function(1, 2, 3, 4, 5, 6, 7, 8, 9))


def my_function(x, **kwargs):
    print(kwargs)
    if x == 0:
        return 'Wrong'
    return x

f = {'1': 0, '2': 1}
print(my_function(1, **f))
print(my_function(1, var1=1, var=2, var3=3))
