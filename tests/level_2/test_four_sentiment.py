from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__good_words_more_than_bad():
    text = ('На кухне приятно пахло свежей выпечкой и ванилью '
            'За окном дрались коты')
    good_words = {'приятно', 'ванилью'}
    bad_words = {'дрались'}

    test = check_tweet_sentiment(text, good_words, bad_words)

    assert test == 'GOOD'


def test__check_tweet_sentiment__bad_words_more_than_good():
    text = ('Незнакомый человек бил тяжелым тупым предметом по голове другого незнакомца'
            ' В комнате так же стояла ваза с красивыми цветами')
    good_words = {'приятно', 'цветами'}
    bad_words = {'тупым', 'бил', 'незнакомца'}

    test = check_tweet_sentiment(text, good_words, bad_words)

    assert test == 'BAD'


def test__check_tweet_sentiment__bad_words_more_than_good():
    text = ('Нейтральный твит про ключевую ставку цб \n'
            'При сохранение текущего уровня бюджетного импульса повышение ключевой ставки '
            'будет только ограничено снижать уровень совокупного спроса, '
            'следовательно повышение ключевой ставки на один процентный пункт будет недостаточно '
            'для достижения таргета по инфляции ')
    good_words = {'таргета', 'бюджетного импульса'}
    bad_words = {'инфляции', 'совокупного спроса'}

    test = check_tweet_sentiment(text, good_words, bad_words)

    assert test == None


def test__check_tweet_sentiment__bad_words_more_than_good():
    text = ('твит про то как увидел на улице кота')
    good_words = {}
    bad_words = {}

    test = check_tweet_sentiment(text, good_words, bad_words)

    assert test == None