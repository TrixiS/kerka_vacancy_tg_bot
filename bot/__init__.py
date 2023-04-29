__title__ = "bot"
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from pathlib import Path

from . import *

ENCODING = "utf-8-sig"
ROOT_PATH = Path(__file__).parent.parent
LOGS_PATH = ROOT_PATH / "logs.log"
