from functions.level_1.one_gender import genderalize


def test__generalize__return_verb_male_when_gender_male():
    verb_male = 'пошел'
    verb_female = 'пошла'
    gender = 'male'

    male_gender_verb = genderalize(verb_male, verb_female, gender)

    assert male_gender_verb == 'пошел'


def test__generalize__return_verb_female_when_gender_female():
    verb_male = 'делал'
    verb_female = 'делала'
    gender = 'female'

    female_gender_verb = genderalize(verb_male, verb_female, gender)

    assert female_gender_verb == 'делала'

