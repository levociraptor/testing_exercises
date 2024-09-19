from functions.level_2.five_replace_word import replace_word

def test__replace_world__base_case():
    text = 'В первой статье о Django мы отвечаем на вопрос «Что такое Django ?» и даём обзор того, что делает его особенным.'
    replace_from = 'Django'
    replace_to = 'Fast Api'

    test = replace_word(text, replace_from, replace_to)

    assert test == 'В первой статье о Fast Api мы отвечаем на вопрос «Что такое Fast Api ?» и даём обзор того, что делает его особенным.'


def test__replace_world__nothing_to_change_case():
    text =  'Мы опишем основные функции, в том числе некоторые из расширенных функций, которые у нас не будет времени подробно рассмотреть в этом модуле'
    replace_from = ''
    replace_to = ''

    test = replace_word(text, replace_from, replace_to)

    assert test == 'Мы опишем основные функции, в том числе некоторые из расширенных функций, которые у нас не будет времени подробно рассмотреть в этом модуле'


def test__replace_world__random_symbol_string_case():
    text = 'asjdfh;asjfg;ajsd;fghasdfgahsfg;ohdsfghiusdhfgi4285ytdifshgl'
    replace_from = 'Hello'
    replace_to = 'Goodbye'

    test = replace_word(text, replace_from, replace_to)

    assert test == 'asjdfh;asjfg;ajsd;fghasdfgahsfg;ohdsfghiusdhfgi4285ytdifshgl'


def test__replace_world__empty_text_string():
    text = ''
    replace_from = 'Hello'
    replace_to = 'Goodbye'

    test = replace_word(text, replace_from, replace_to)

    assert test == ''