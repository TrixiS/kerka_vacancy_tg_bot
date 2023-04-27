from dataclasses import dataclass


@dataclass
class BotPhrases:
    start_message_text_fmt = """Привет, {full_name}
Сообщение пользователю:
Я - бот для пополнения баланса. 
Нажмите на кнопку, чтобы пополнить баланс"""
    deposit_button_text = "Пополнить баланс"


PHRASES = BotPhrases()
