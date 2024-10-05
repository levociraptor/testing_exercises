from functions.level_2.five_replace_word import replace_word


def test__replace_world__return_modified_text():
    text = 'В первой статье о Django мы отвечаем на вопрос «Что такое Django ?»'
    replace_from = 'Django'
    replace_to = 'Fast Api'

    replaced_text = replace_word(text, replace_from, replace_to)

    assert replaced_text == 'В первой статье о Fast Api мы отвечаем на вопрос «Что такое Fast Api ?»'


def test__replace_world__return_text_without_changes_when_replace_from_is_empty():
    text = 'Мы опишем основные функции, в том числе некоторые из расширенных функций'

    replaced_text = replace_word(text, '', 'крабы')

    assert replaced_text == 'Мы опишем основные функции, в том числе некоторые из расширенных функций'


def test__replace_world__return_modified_text_without_words_specified_in_replace_from():
    text = 'Мы опишем основные функции, в том числе некоторые из расширенных функций'
    replace_from = 'функций'

    replaced_text = replace_word(text, replace_from, '')

    assert replaced_text == 'Мы опишем основные функции, в том числе некоторые из расширенных '


def test__replace_world__return_original_text():
    text = 'asjdfh;asjfg;ajsd;fghasdfgahsfg;ohdsfghiusdhfgi4285ytdifshgl'
    replace_from = 'Hello'
    replace_to = 'Goodbye'

    replaced_text = replace_word(text, replace_from, replace_to)

    assert replaced_text == 'asjdfh;asjfg;ajsd;fghasdfgahsfg;ohdsfghiusdhfgi4285ytdifshgl'


def test__replace_world__return_empty_string_when_text_is_empty():
    text = ''
    replace_from = 'Hello'
    replace_to = 'Goodbye'

    replaced_text = replace_word(text, replace_from, replace_to)

    assert replaced_text == ''
