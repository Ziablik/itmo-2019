def my_sum(first_num, secound_num):
    return first_num + secound_num


def test_sum():
    assert my_sum(1, 3) == 3
    assert round(my_sum(2.1, 4.2), 2) == 6.3


if __name__ == '__main__':
    try:
        test_sum()
        print('ok')
    except AssertionError:
        print('fail')
