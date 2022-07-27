import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15473091"))
    API_HASH = os.environ.get("API_HASH", "34c239eef99eb51659cb60b2e3927182")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MusicplayNikkibot")
    SUPPORT = os.environ.get("SUPPORT", "MyBotSupport")
    CHANNEL = os.environ.get("CHANNEL", "")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/18b5cd1061adfe09f7459.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", ""))
