# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("26556200"))
    API_HASH = os.environ.get("3917b963bcc9a867097c4811af6ab39d")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("AQGVNygApD2DypYqDvMp3Xg9oJwtHTou7DGyI_wcCZhV4NOasgQ1Y5PL9CTILDmSTc_VScI7sD6CazDiu7PgJdJzLB0pBpeC_Zr80UkyVJfMLloQi53f7mrJWXBdpjxMkuIBt7Sm9uepuinZGz_JTwiXFw9OIs_qLMcI5JJl2-ObvA3rnXyPCf75dqCl8RTIVxYMQ3A7Kp1AbGlR7q_nI7JPVwnx8Kw-rQkTavW5QEvgaDvgVyK_qrWdkcfTkLql-hRvUX5nJ1MeBH-oT0HerscJjxdDPjtN52br_B9lCblMwKzlC-Fnsg3nSzReqIhpEOMWqXVe710Rvc2hQ8pb0alHR0YF1wAAAAGP0sIxAA")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-1002105476348").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-1002364591403").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
