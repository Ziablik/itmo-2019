# -*- coding: utf-8 -*-


def my_sum(first_num, second_num):
    """Returns sum."""                          # noqa: DAR101, DAR201
    return first_num + second_num


def test_sum():
    """Test for my_sum function."""
    assert my_sum(1, 2) == 3
    assert round(my_sum(2.1, 4.2), 2) == 6.3    # noqa: WPS432


if __name__ == '__main__':
    try:
        test_sum()
    except AssertionError:
        print('fail')                           # noqa: T001
    else:
        print('ok')                             # noqa: T001
