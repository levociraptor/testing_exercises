import pytest

from functions.level_2.three_first import first


def test__first__return_firts_element_of_the_sequence():
    items = [13, 23, 67, 56]

    test = first(items)

    assert test == 13


def test__first__raise_exception_when_sequence_is_empty_and_no_default():
    items = []
    with pytest.raises(AttributeError):
        first(items)


def test__first__return_default_when_empty_sequence():
    items = []
    default = 'asdasd'

    test = first(items, default)

    assert test == 'asdasd'


def test__first__return__empty_string_when_empty_sequence_and_default_is_empty_string():
    items = []
    default = ''

    test = first(items, default)

    assert test == ''

