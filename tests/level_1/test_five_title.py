from functions.level_1.five_title import change_copy_item


def test__change_copy_item__return_title_with_copy_of():
    assert change_copy_item('Hello world') == 'Copy of Hello world'


def test__change_copy_item__return_unchanged_title_when_title_mora_than_max_title_len():
    assert change_copy_item('Hello world', 5) == 'Hello world'


def test__change_copy_item__return_title_with_number_on_brackets_when_title_start_with_copy_of():
    assert change_copy_item('Copy of something') == 'Copy of something (2)'


def test__change_copy_item__return_title_with_increased_number_when_title_have_number_in_brackets():
    assert change_copy_item('Copy of something (25)') == 'Copy of something (26)'

