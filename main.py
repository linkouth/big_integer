import re
from datetime import datetime
from big_integer import BigInt


def handle_exponentiation(a, b, c):
    if int(str(c)) <= 0:
        print('Модуль должен быть больше нуля')
        return
    # Сравнение времени работы возведения в степень по модулю
    time_exp_start = datetime.now()
    if int(str(a)) == 0 and int(str(b)) == 0:
        if int(str(c)) > 1:
            exp_result = BigInt('1')
    else:
        exp_result = a.pow(b, c)
    if int(str(c)) == 1:
        exp_result = BigInt('0')
    time_exp_end = datetime.now()
    time_build_exp_start = datetime.now()
    build_in_exp = pow(int(str(a)), int(str(b)), int(str(c)))
    time_build_exp_end = datetime.now()

    print('a ^ b mod c = ', end='')
    print(exp_result)

    print('--------------------------------------------------')
    print('Верно: ', end='')
    print(int(str(exp_result)) == build_in_exp)
    print('Время работы реализации по Кнуту: ', end=' ')
    print(time_exp_end - time_exp_start)
    print('Время работы встроенной реализации:', end=' ')
    print(time_build_exp_end - time_build_exp_start)
    print()


def main():
    while True:
        not_number = re.compile(r'^[-]?[0-9]+$')
        s = input('Введите число-основание: ')
        while not not_number.match(s):
            print('Некорретное число')
            s = input('Введите число-основание: ')

        a = BigInt(s)

        s2 = input('Введите число-показатель: ')
        while not not_number.match(s2):
            print('Некорретное число')
            s2 = input('Введите число-показатель: ')

        b = BigInt(s2)

        s3 = input('Введите число-модуль: ')
        while not not_number.match(s3):
            print('Некорретное число')
            s3 = input('Введите число-модуль: ')

        c = BigInt(s3)

        handle_exponentiation(a=a, b=b, c=c)


if __name__ == '__main__':
    main()
