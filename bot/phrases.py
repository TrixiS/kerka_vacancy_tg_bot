from dataclasses import dataclass


@dataclass
class AdminPhrases:
    admin_message_text = "Админка"
    export_users_button_text = "Выгрузить пользователей"
    export_logs_button_text = "Выгрузить логи"
    set_balance_button_text = "Изменить баланс"
    ban_user_button_text = "Заблокировать пользователя"
    enter_user_id_message_text = "Введите ID пользователя"
    enter_amount_message_text = "Введите сумму"
    set_balance_message_text = "Баланс установлен"
    ban_user_message_text = "Пользователь заблокирован"


@dataclass
class BotPhrases:
    admin = AdminPhrases()
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
