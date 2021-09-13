from random import randint
def task_1():
    with open('home_work_file', 'r') as f:
        def my_gen(text):
            for x in range(text):
                yield x
        print(my_gen(f.readlines()))


def task_2(values):
    def my_map(func, args):
        my_str = args[0].lower()
        for i in args[1:]:
            my_str += func(i)
        return my_str

    def my_func(args):
        if args.isupper():
            return '_'+args.lower()
        else:
            return args

    return my_map(my_func, values)

def task_3(my_str):
    return (lambda x: x == x[::-1])("корок")

def task_4():
    N = randint(1, 100)
    while True:
        version = input()
        if version == '>':
            N = randint(N, 100)
            return N
        elif version == '<':
            return lambda x: randint(0, x)
        elif version == '=':
            pass
        else:
            print()
    lambda x: randint(0, x)

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
                task_1()
            elif task == 2:
                print(task_2('CamelCase'))
            elif task == 3:
                print((lambda x: x == x[::-1])("корок"))
            elif task == 4:
                pass
            elif task == 5:
                pass
        elif task == 'end':
            print('Завершення програми!')
            break
        else:
            print('Некоректне значення!')
            continue


if __name__ == '__main__':
    main()