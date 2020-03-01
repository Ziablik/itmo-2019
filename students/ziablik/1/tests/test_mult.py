# -*- coding: utf-8 -*-


def my_mult(first_num, second_num):
    """Returns mult."""             # noqa: DAR101, DAR201
    return first_num * second_num


def test_mult():
    """Test for my_sum function."""
    assert my_mult(-6, -4) == 24


if __name__ == '__main__':
    try:
        test_mult()
    except AssertionError:
        print('fail')               # noqa: T001
    else:
        print('ok')                 # noqa: T001
