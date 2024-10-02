import pytest

from functions.level_1.one_gender import genderalize

@pytest.mark.parametrize(
    'verb_male,verb_female,gender,expected_result',
    [
        ('пошел', 'пошла', 'male', 'пошел'),
        ('делал', 'делала', 'female', 'делала')
    ]

)
def test__generalize__return_verb_of_the_specified_gender(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
