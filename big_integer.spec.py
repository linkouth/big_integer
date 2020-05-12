from big_integer import BigInt


def test_all():
    test_adding()
    test_subtracting()


def test_adding():
    n = 10000
    is_correct = True
    for i in range(n // 10, n):
        a = BigInt(str(i))
        for j in range(n // 10, n):
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



def main():
    test_all()


if __name__ == '__main__':
    main()
