from functions.level_1.two_date_parser import compose_datetime_from
from datetime import datetime, time, date, timedelta


def test__compose_datetime_from__return_today_date_with_time_str():
    date_str = ''
    time_str = '10:30'

    today_date = datetime.combine(date.today(), time(10, 30))
    function_result = compose_datetime_from(date_str, time_str)

    assert today_date == function_result


def test__compose_datetime_from__return_tomorrow_date_when_date_str_is_tomorrow():
    date_str = 'tomorrow'
    time_str = '13:04'

    tomorrow_date = datetime.combine(date.today() + timedelta(days=1), time(13, 4))
    function_result = compose_datetime_from(date_str, time_str)

    assert tomorrow_date == function_result
