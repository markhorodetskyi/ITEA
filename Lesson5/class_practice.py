# file = open('text_file', 'a')
#
# while True:
#     line = input("Enter name and surname: ")
#     if not line:
#         break
#     else:
#         file.write(f'{line}\n')
# file.close()

# with open('text_file', 'r') as file:
#     read = file.read()
#     print(read.split(' '))
#     count = 0
#
#     for words in read.split(' '):
#         if "orem" in words:
#             print(words)
#             count += 1
#     read.replace("Lorem", 'Mark')
#     print(read)
#     print(f'Знайдено {count} слів "Lorem"')

new_file = open('new_practice_file', "w")

data = '''Авраменко 3
Авратинський 4
Адамович 5
Бабич 2
Бабиченко 4
Бабій 3
Дерев'янко 5'''


new_file.write(data)
new_file = open('new_practice_file', "r")
# print(new_file.read())
for line in new_file.readlines():
    student = line.split(' ')
    if int(student[1]) > 3:
        print(student[0])
