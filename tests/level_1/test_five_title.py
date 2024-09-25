from functions.level_1.five_title import change_copy_item


def test__change_copy_item__return_title_with_string_copy_of_when_tittle_doesnt_start_with_copy_of():
    title = 'Hello world'

    result = change_copy_item(title)

    assert result == 'Copy of Hello world'


def test__change_copy_item__return_title():
    title = 'Hello world'
    max_main_item_title_length = 5

    result = change_copy_item(title, max_main_item_title_length)

    assert result == 'Hello world'


def test__change_copy_item__return_title_with_number_on_brackets_when_title_start_with_copy_of():
    title = 'Copy of something'

    result = change_copy_item(title)

    assert result == 'Copy of something (2)'


def test__change_copy_item__return_title_with_increased_number_when_title_have_number_in_brackets():
    title = 'Copy of something (25)'

    result = change_copy_item(title)

    assert result == 'Copy of something (26)'

