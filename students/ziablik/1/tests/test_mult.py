def my_mult(first_num, secound_num):
    return first_num * secound_num


def test_mult():
    assert my_mult(-6, -4) == 24


if __name__ == '__main__':
    try:
        test_mult()
        print('ok')
    except AssertionError:
        print('fail')