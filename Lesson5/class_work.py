import random
# new_lst = [1, 2, 3, 4]
#
# if 1 in new_lst:
#     print("1")
# elif 2 in new_lst:
#     print('2')
# else:
#     print('NO')
#
# flag = True
# while flag:
#     print('Hello')
#
# card = 1000
#
# while  card > 0:
#     x = input('How much we spent ')
#     card -= int(x)
#     print(f'{card} left')
#     if card <= 500:
#         print('Stop spending')
#         break

# count = 0
# while True:
#     count += 1
#     value = random.randint(0, 10)
#     if value == 0:
#         break
#     elif value % 2 > 0:
#         continue
#     print(f'Count: {count} value - {value}')
#

# file = open('text_file', 'a')
# # print(file.read())
# # for line in file.readlines():
# #     print(line.lower())
# 
# while True:
#     line = input("Enter name and surname: ")
#     if not line:
#         break
#     else:
#         file.write(f'{line}\n')
# file.close()

import pickle


my_list = [123, 'John', 356.0, 1+2j]

pickle.dump(my_list, open('new_pick', 'wb'))
print(pickle.load(open('new_pick', 'rb')))
