from functions.level_1.four_bank_parser import (BankCard,
                                                SmsMessage, Expense, parse_ineco_expense)
from datetime import datetime
import decimal


def test__parse_ineco_expense__return_expense_object():
    sms = SmsMessage(text="123.45 USD, Visa1234 25.12.23 18:30 store authcode 324234",
                     author='Lev Uspensky',
                     sent_at=datetime(2023, 12, 25, 18, 30))
    cards = [BankCard(last_digits='1234', owner='Lev Uspensky'),
             BankCard(last_digits='8923', owner='Vasiluy Petrov')]
    expense = Expense(
        amount=decimal.Decimal('123.45'),
        card=BankCard(last_digits='1234', owner='Lev Uspensky'),
        spent_in='store',
        spent_at=datetime(2023, 12, 25, 18, 30)
    )

    result = parse_ineco_expense(sms, cards)

    assert result == expense

