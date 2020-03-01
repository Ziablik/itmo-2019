# -*- coding: utf-8 -*-


def my_div(first_num, second_num):
    """Returns div."""          # noqa: DAR101,DAR201
    return first_num / second_num


def test_div():                 # noqa: WPS218
    """Test for my_div function."""
    assert my_div(1, 1) == 1
    assert isinstance(my_div(1, 1), float)
    assert my_div(5, 2) == 2.5  # noqa: WPS432
    assert my_div(6, 2) == 3.0  # noqa: WPS432

    try:
        my_div(1, 0)
    except ZeroDivisionError:
        assert True             # noqa: WPS444
    else:
        assert False            # noqa: B011,WPS444


if __name__ == '__main__':
    try:
        test_div()
    except AssertionError:
        print('fail')           # noqa: T001
    else:
        print('ok')             # noqa: T001
