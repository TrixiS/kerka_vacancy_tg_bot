from dataclasses import dataclass


@dataclass
class BotPhrases:
    start_message_text_fmt = """Привет, {full_name}
Сообщение пользователю:
Я - бот для пополнения баланса. 
Нажмите на кнопку, чтобы пополнить баланс"""
    deposit_button_text = "Пополнить баланс"
    enter_deposit_amount_message_text = (
        "Введите сумму, на которую вы хотите пополнить баланс"
    )
    invalid_deposit_amount_message_text = "Вы ввели неверную сумму пополнения"
    bill_message_text = 'Нажмите на кнопку "Оплатить", чтобы совершить оплату. После оплаты нажмите на кнопку "Проверить оплату"'
    pay_button_text = "Оплатить"
    check_payment_button_text = "Проверить оплату"
    unpaid_bill_answer_text = "Вы не оплатили счет"
    deposit_message_text = "Баланс пополнен"


PHRASES = BotPhrases()
