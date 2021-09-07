



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
                pass
            elif task == 2:
                pass
            elif task == 3:
                pass
        elif task == 'end':
            print('Завершення програми!')
            break
        else:
            print('Некоректне значення!')
            continue


if __name__ == '__main__':
    main()