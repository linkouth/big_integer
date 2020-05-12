from big_integer import BigInt


def test_all():
    test_subtracting()


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
