from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('пошел', 'пошла', 'male') == 'пошел'
    assert genderalize('делал', 'делала', 'female') == 'делала'
