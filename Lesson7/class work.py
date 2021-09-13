import Lesson7.test1.test1

x = 99


def f1():
    x = 88

    def f2():
        print(x)
    f2()


def maker(N):
    def action(X):
        return X ** N
    return action


def change_name(name):
    def change_name2():
        return name.upper()
    return change_name2


def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 2
    return nested

def county(code):
    def number(number):
        print(f'Країна - {code}, код')


def test_1():
    print(Lesson7.test1.test1.x)

if __name__ == '__main__':
    # f1()
    # print(maker(3)(3))
    # print(change_name('mark')())
    test_1()