def my_div(first_num, secound_num):
    return first_num / secound_num


def test_div():
    assert my_div(1, 1) == 1
    assert isinstance(my_div(1, 1), float)
    assert my_div(5, 2) == 2.5
    assert my_div(6, 2) == 3.0

    try:
        my_div(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False


if __name__ == '__main__':
    try:
        test_div()
        print('ok')
    except AssertionError:
        print('fail')