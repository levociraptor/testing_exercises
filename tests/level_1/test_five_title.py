from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('Hello world') == 'Copy of Hello world'
    assert change_copy_item('Hello world', 5) == 'Hello world'
    assert change_copy_item('Copy of something') == 'Copy of something (2)'
    assert change_copy_item('Copy of something(25)') == 'Copy of (26)'

