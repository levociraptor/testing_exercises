import pytest

from functions.level_2.three_first import first

def test__first__base_case():
    items = [13, 23, 67, 56]

    test = first(items)

    assert test == 13


def test__first__exception_raise():
    items = []
    default = "NOT_SET"

    with pytest.raises(AttributeError):
        first(items, default)


def test__first__empty_list():
    items = []
    default = 'default'

    test = first(items, default)

    assert test == 'default'


def test__first__empty_list_empty_default():
    items = []
    default = ''

    test = first(items, default)

    assert test == ''

