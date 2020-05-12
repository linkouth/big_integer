from big_integer import BigInt


def test_all():
    test_adding()
    test_subtracting()
    test_division()
    test_exponentiation()


def test_adding():
    n = 1000
    is_correct = True
    for i in range(1, n):
        a = BigInt(str(i))
        for j in range(1, n // 10):
            b = BigInt(str(j))
            custom_result = a.add(b)
            build_in_result = i + j
            if int(str(custom_result)) != build_in_result:
                print(f'{str(custom_result)} is not equal to {build_in_result}')
                is_correct = False
                break
    if is_correct:
        print('Adding is correct')
    else:
        print('Adding is not correct')


def test_subtracting():
    n = 1000
    is_correct = True
    for i in range(1, n):
        a = BigInt(str(i))
        for j in range(1, n // 10):
            b = BigInt(str(j))
            custom_result = a.subtract(b)
            build_in_result = i - j
            if int(str(custom_result)) != build_in_result:
                print(f'{str(custom_result)} is not equal to {build_in_result}')
                is_correct = False
                break
    if is_correct:
        print('Subtracting is correct')
    else:
        print('Subtracting is not correct')


def test_division():
    n = 5000
    m = 250
    is_correct = True
    for i in range(1, n):
        a = BigInt(str(i))
        for j in range(1, m):
            b = BigInt(str(j))
            custom_result = a.div(b)
            build_in_result = i // j
            if int(str(custom_result)) != build_in_result:
                print(f'{str(custom_result)} is not equal to {build_in_result}')
                is_correct = False
                break
    if is_correct:
        print('Division is correct')
    else:
        print('Division is not correct')


def test_exponentiation():
    n = 25
    m = 25
    c = 20
    is_correct = True
    for i in range(1, n):
        a = BigInt(str(i))
        for j in range(1, m):
            b = BigInt(str(j))
            for k in range(1, c):
                mod = BigInt(str(k))
                custom_result = a.pow(b, mod)
                build_in_result = pow(i, j, k)
                if int(str(custom_result)) != build_in_result:
                    print(f'{str(custom_result)} is not equal to {build_in_result}')
                    is_correct = False
                    break
    if is_correct:
        print('Exponentiation is correct')
    else:
        print('Exponentiation is not correct')


def main():
    test_all()


if __name__ == '__main__':
    main()
