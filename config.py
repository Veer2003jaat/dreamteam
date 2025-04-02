import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7557588543:AAHUreOzyi5Sak9DNp297RGZGXUT47vDSUQ"
    # Telegram API ki ID
    API_ID = 26307640
    # Telegram API ki hash key
    API_HASH = "e8b89d09e2e752c7034f497322f0e20a"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '6133985472'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://amazingyaan:qFyyF41iELawTZmM@dreamtxup.vopl4qw.mongodb.net/?retryWrites=true&w=majority&appName=dreamtxup"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002565842447
    # Authentication log channel ki ID
    AUTH_LOG = -1002565842447
    # Hit log channel ki ID
    HIT_LOG = -1002565842447
    # DRM dump channel ki ID
    DRM_DUMP = -1002565842447
    # Main channel ki ID
    CHANNEL = -1002565842447
    # Channel ka link
    CH_URL = "https://t.me/Dreambatches"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Dreamteamapp"
    # Thumbnail image ka URL
    THUMB_URL = "https://te.legra.ph/file/11366447de3410810a383-d29ae883f7add39f2a.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

