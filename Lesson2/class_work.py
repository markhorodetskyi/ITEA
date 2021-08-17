import datetime

def print_hi():
    print('1')
    in_name = input('Please enter your name:')
    print(f'Welcome ,{in_name}!')

def sum_numbers():
    print('2')
    loop = True
    while(loop):
        digits1 = input('Please enter first number:')
        if digits1.isdigit():
            digits1 = int(digits1)
            digits2 = input('Please enter second number:')
            if digits2.isdigit():
                digits2 = int(digits2)
                print(f'Sum two numbers - {digits1 + digits2}!')
                loop = False
            else:
                print('Its not number')
        else:
            print(f'Its not number!')

def ages():
    print('3')
    in_name = input('Please enter your name:')
    print(f'Welcome ,{in_name}!')
    age = input('Please enter your age:')
    if age.isdigit():
        age = int(age)
        to_year = 100 - age
        now_date = datetime.datetime.now()
        date_to_end = now_date.replace(year=now_date.year + to_year)
        print(f'You finish in {date_to_end.year} :)')
    else:
        print('Its not number')

def digits():
    print('4')
    loop = True
    while (loop):
        digits1 = input('Please enter number:')
        if digits1.isdigit():
            digits1 = int(digits1)
            if digits1 > 0:
                if digits1 % 2 > 0:
                    print(f'Число {digits1} не парне.')
                    loop = False
                else:
                    print(f'Число {digits1} парне.')
                    loop = False
            else:
                print(f'Число менше або дорівнює нулю')
        else:
            print('Its not number')

def digits2():
    print('5')
    digits1 = input('Please enter number:')
    loop = True
    while (loop):
        if digits1.isdigit():
            digits1 = int(digits1)
            if digits1 > 0:
                digits1 = digits1 + (digits1**digits1) + (digits1*digits1*digits1)
                print(f'n + (n**n) + (n*n*n) = {digits1}. Не впевнений що зрозумів завдання')
                loop = False
            else:
                print(f'Число менше або дорівнює нулю')
        else:
            print('Its not number')

if __name__ == '__main__':
    # print_hi()
    # sum_numbers()
    # ages()
    digits()
    digits2()