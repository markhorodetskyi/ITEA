def task_1(x):
    if len(x) < 3:
        print('Кортеж замалий')
        return
    else:
        return x[-1], x[-3], x[-2]


def task_2(x):
    my_list = x.split(' ')
    my_list2 = []
    for i in my_list:
        if not i.isdigit():
            print(f'Елемент списку "{i}", не є числом. Його буде видалено')
        elif i.isdigit():
            my_list2.append(int(i))
    result = 1
    for i in my_list2:
        if i != 0:
            result *= i
    return result


def task_3(x):
    result = ''
    for letter in x:
        if letter.isupper():
            result += letter
    return result

"""
1.Написати функцію яка приймає список і повертає всі числа які знаходяться перед найбільшим числом з цього списку. [ 1, 6, 5, 10, 8, 7 ] -> 1,6,5

2.Написати функцію яка приймає словник де ключ це число а значення це список. Функція має повернути цей словник, почистивши всі дуплікати в списку значень.
input = {
  "432": ["A", "A", "B", "D"],
  "53": ["L", "G", "B", "C"],
  "236": ["L", "A", "X", "G", "H", "X"],
  "11": ["P", "R", "S", "D"],
}

output = {
  "11": ["P", "R", "S"],
  "53": ["C"],
  "236": ["L", "X", "G", "H"],
  "432": ["A", "B", "D"],
}

"""

def task_4(x):
    maxi = max(x)
    for i in x:
        if i != maxi:
            print(f'{i} ', end='')
        elif i == maxi:
            print('')
            break


def task_5(x):
    del_letter = []
    my_list = []
    for value in x.values():
        my_list += value
    save_letter = ''
    for letter in sorted(my_list):
        if save_letter == letter:
           del_letter.append(letter)

    for letter in del_letter:
        for key, value in x.items():
            for dict_letter in value:
                if letter == dict_letter:
                    x[key].remove(letter)



def main():
    main_loop = True
    while main_loop:
        print('-------------------------------------')
        print('')
        print('1. Завдання 1. ')
        print('2. Завдання 2. ')
        print('3. Завдання 3. ')
        print('4. Завдання 4. ')
        print('5. Завдання 5. ')
        print('Будь ласка введіть номер 1 - 5, або "end" для завершення програми: ')
        task = input()
        if task.isdigit():
            task = int(task)
            if task == 1:
                print(task_1((1, 2, 3)))
            elif task == 2:
                print(task_2('1 0 ds 4 -2 f 3'))
            elif task == 3:
                print(task_3('How are you? Eh, ok. Low or Lower? Ohhh.'))
            elif task == 4:
                task_4([1, 6, 5, 10, 8, 7])
            elif task == 5:
                my_dict = {
                    "432": ["A", "A", "B", "D"],
                    "53": ["L", "G", "B", "C"],
                    "236": ["L", "A", "X", "G", "H", "X"],
                    "11": ["P", "R", "S", "D"],
                }
                task_5(my_dict)
        elif task == 'end':
            print('Завершення програми!')
            break
        else:
            print('Некоректне значення!')
            continue


if __name__ == '__main__':
    main()