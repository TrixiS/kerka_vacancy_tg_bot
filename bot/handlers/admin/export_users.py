from io import BytesIO

from aiogram import types
from prisma.models import BotUser

from ...bot import DISPATCHER
from ...phrases import PHRASES


@DISPATCHER.message_handler(lambda m: m.text == PHRASES.admin.export_users_button_text)
async def export_users_handler(message: types.Message):
    bot_users = await BotUser.prisma().find_many()

    bot_users_fmt = "\n".join(
        f"{bot_user.id} {bot_user.balance} RUB" for bot_user in bot_users
    )

    buffer = BytesIO(bot_users_fmt.encode())
    input_file = types.InputFile(buffer, filename="users.txt")
    await message.answer_document(input_file)
