from io import BytesIO

import aiofiles
from aiogram import types

from ... import LOGS_PATH
from ...bot import DISPATCHER
from ...phrases import PHRASES


@DISPATCHER.message_handler(lambda m: m.text == PHRASES.admin.export_logs_button_text)
async def export_logs_handler(message: types.Message):
    async with aiofiles.open(LOGS_PATH, "rb") as f:
        buffer = BytesIO(await f.read())

    input_file = types.InputFile(buffer, filename="logs.txt")
    await message.answer_document(input_file)
