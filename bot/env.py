from pathlib import Path

from pydantic import BaseSettings

from . import ENCODING, ROOT_PATH


class ENV(BaseSettings):
    bot_token: str
    admin_user_id: int | str
    qiwi_p2p_key: str

    class Config:
        env_file = ROOT_PATH / ".env"
        env_file_encoding = ENCODING


env = ENV()  # type: ignore
