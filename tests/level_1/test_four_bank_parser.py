import pytest

from functions.level_1.four_bank_parser import (BankCard,
                                                SmsMessage, parse_ineco_expense)
from datetime import datetime
import decimal


def test__parse_ineco_expense__return_amount_equal_amount_in_sms():
    sms = SmsMessage(text="123.4534567 USD, Visa1234 25.12.23 18:30 store authcode 324234",
                     author='Lev Uspensky',
                     sent_at=datetime(2023, 12, 25, 18, 30))
    cards = [BankCard(last_digits='1234', owner='Lev Uspensky'),
             BankCard(last_digits='8923', owner='Vasiluy Petrov')]

    result = parse_ineco_expense(sms, cards)

    assert result.amount == decimal.Decimal('123.4534567')


def test__parse_ineco_expense__return_BankCard_in_result():
    sms = SmsMessage(text="123.4534567 USD, Visa1234 25.12.23 18:30 store authcode 324234",
                     author='Lev Uspensky',
                     sent_at=datetime(2023, 12, 25, 18, 30))
    cards = [BankCard(last_digits='1234', owner='Lev Uspensky'),
             BankCard(last_digits='8923', owner='Vasiluy Petrov')]

    result = parse_ineco_expense(sms, cards)

    assert result.card == BankCard(last_digits='1234', owner='Lev Uspensky')


def test__parse_ineco_expense__return_spentin_equal_spentin_in_sms():
    sms = SmsMessage(text="123.4534567 USD, Visa1234 25.12.23 18:30 store authcode 324234",
                     author='Lev Uspensky',
                     sent_at=datetime(2023, 12, 25, 18, 30))
    cards = [BankCard(last_digits='1234', owner='Lev Uspensky'),
             BankCard(last_digits='8923', owner='Vasiluy Petrov')]

    result = parse_ineco_expense(sms, cards)

    assert result.spent_in == 'store'


def test__parse_ineco_expense__return_spent_at_equal_datetime_in_sms():
    sms = SmsMessage(text="123.4534567 USD, Visa1234 25.12.23 18:30 store authcode 324234",
                     author='Lev Uspensky',
                     sent_at=datetime(2023, 12, 25, 18, 30))
    cards = [BankCard(last_digits='1234', owner='Lev Uspensky'),
             BankCard(last_digits='8923', owner='Vasiluy Petrov')]

    result = parse_ineco_expense(sms, cards)

    assert result.spent_at == datetime(2023, 12, 25, 18, 30)


def test__parse_ineco_expense__return_exception_when_card_in_sms__not_compare_with_BankCard_in_cards():
    sms = SmsMessage(text="123.4534567 USD, Visa1243 25.12.23 18:30 store authcode 324234",
                     author='Lev Uspensky',
                     sent_at=datetime(2023, 12, 25, 18, 30))
    cards = [BankCard(last_digits='1234', owner='Lev Uspensky'),
             BankCard(last_digits='8923', owner='Vasiluy Petrov')]

    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards)
