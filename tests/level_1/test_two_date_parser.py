from functions.level_1.two_date_parser import compose_datetime_from
from datetime import datetime, time, date, timedelta


def test_compose_datetime_from():
    assert compose_datetime_from('', '10:30') == datetime.combine(
        date.today(),
        time(10, 30)
    )

    tomorrow_date = date.today() + timedelta(days=1)
    assert compose_datetime_from('tomorrow', '13:04') == datetime.combine(
        tomorrow_date,
        time(13, 4)
    )