import re
from datetime import datetime
from big_integer import BigInt


def handle_division(a, b):
    div_result = None
    mod_result = None
    s = a
    s2 = str(b)
    if int(s2) != 0:
        time_div_start = datetime.now()
        div_result = a.div(b)
        time_div_end = datetime.now()
        time_mod_start = datetime.now()
        mod_result = a.rem(b)
        time_mod_end = datetime.now()
    else:
        # Обработка ошибок
        print('Error division by zero')

    # Вывод результата деления
    time_build_div_start = datetime.now()
    time_build_div_end = datetime.now()
    time_build_mod_start = datetime.now()
    time_build_mod_end = datetime.now()

    print()
    print('--------------------------------------------------')
    print('a / b = ', end='')
    print(div_result)

    print()
    print('--------------------------------------------------')
    print('a % b = ', end='')
    print(mod_result)

    print()
    print('--------------------------------------------------')
    print('Сравнение времени работы')
    print('Реализация по Кнуту за ', end=' ')
    print(time_div_end - time_div_start)
    print('Встроенная реализация за', end=' ')
    print(time_build_div_end - time_build_div_start)

    print()
    print('--------------------------------------------------')
    print('Result of MOD')
    print('Custom in ', end=' ')
    print(time_mod_end - time_mod_start)
    print('Build in ', end=' ')
    print(time_build_mod_end - time_build_mod_start)


def handle_adding(a, b):
    s = str(a)
    s2 = str(b)
    print('a + b = ', end='')
    print(a.add(b))

    time_add_start = datetime.now()
    result = a.add(b)
    time_add_end = datetime.now()
    time_add_build_add_start = datetime.now()
    time_add_build_add_end = datetime.now()
    print()
    print('--------------------------------------------------')
    print('Result of ADDING')
    print(int(str(result)) == (int(s) + int(s2)))
    print('Custom in', end='')
    print(time_add_end - time_add_start)
    print('Build in', end='')
    print(time_add_build_add_end - time_add_build_add_start)


def handle_subtracting(a, b):
    s = str(a)
    s2 = str(b)
    print('a - b = ', end='')
    print(a.subtract(b))

    time_subtract_start = datetime.now()
    result = a.subtract(b)
    time_subtract_end = datetime.now()
    time_add_build_subtract_start = datetime.now()
    time_add_build_subtract_end = datetime.now()

    print()
    print('--------------------------------------------------')
    print('Result of SUBTRACTION')
    print(int(str(result)) == (int(s) - int(s2)))
    print('Custom in', end='')
    print(time_subtract_end - time_subtract_start)
    print('Bbuild in', end='')
    print(time_add_build_subtract_end - time_add_build_subtract_start)


def handle_multiplication(a, b):
    s = str(a)
    s2 = str(b)

    print('a * b = ', end='')
    print(a.multiply(b))

    time_multiple_start = datetime.now()
    result = a.multiply(b)
    time_multiple_end = datetime.now()
    time_multiple_build_start = datetime.now()
    time_multiple_build_end = datetime.now()

    print()
    print('--------------------------------------------------')
    print('Result of MULTIPLICATION')
    print(int(str(result)) == (int(s) * int(s2)))
    print('Custom in', end='')
    print(time_multiple_end - time_multiple_start)
    print('Build in', end='')
    print(time_multiple_build_end - time_multiple_build_start)


def handle_exponentiation(a, b, c):
    # Сравнение времени работы возведения в степень по модулю
    time_exp_start = datetime.now()
    exp_result = a.pow(b, c)
    time_exp_end = datetime.now()
    time_build_exp_start = datetime.now()
    build_in_exp = pow(int(str(a)), int(str(b)), int(str(c)))
    time_build_exp_end = datetime.now()

    print('a ^ b mod c = ', end='')
    print(exp_result)

    print()
    print('--------------------------------------------------')
    print('Result of EXPONENTIATION')
    print(int(str(exp_result)) == build_in_exp)
    print('Custom in ', end=' ')
    print(time_exp_end - time_exp_start)
    print('Build in ', end=' ')
    print(time_build_exp_end - time_build_exp_start)


def main():
    not_number = re.compile(r'^[-]?[0-9]+$')
    s = input('Input the first number: ')
    while not not_number.match(s):
        print('Incorrect number')
        s = input('Input the first number: ')

    a = BigInt(s)

    s2 = input('Input the second number: ')
    while not not_number.match(s2):
        print('Incorrect number')
        s2 = input('Input the second number: ')

    b = BigInt(s2)

    s3 = input('Input the second number: ')
    while not not_number.match(s3):
        print('Incorrect number')
        s3 = input('Input the second number: ')

    c = BigInt(s3)

    handle_adding(a=a, b=b)
    handle_subtracting(a=a, b=b)
    handle_multiplication(a=a, b=b)
    handle_division(a=a, b=b)
    handle_exponentiation(a=a, b=b, c=c)


if __name__ == '__main__':
    main()
