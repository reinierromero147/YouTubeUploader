import os


class Config:

    BOT_TOKEN = os.environ.get("6660807180:AAFtVdxLF2XngwzYJLY_xgTcws3zrlupB_Y")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("20946968"))

    API_HASH = os.environ.get("2e51eed71c861b8f030f959bc34c5167")

    CLIENT_ID = os.environ.get("473810559979-b0nuk0tbb57at6ia16ltg8ukdiltdfdp.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("1437976419"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 1437976419] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
