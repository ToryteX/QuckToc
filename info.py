import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class pirobot(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
# Bot images & videos
PICS = (environ.get('PICS', 'https://telegra.ph/file/5553dc39f968b364d4856.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/0593a3103ba1b9a5855bf.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/485b93dd1ec801061f091.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/2a888a370f479f4338f7c.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "PIRO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'FILES')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'raixchat')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '<b>╭──[𝑹𝑹_𝒓𝒆𝑸]───⧐</b> \n<b>│</b> \n<b>├⍟ 🗂 𝑭𝒊𝒍𝒆 𝑵𝒂𝒎𝒆 : <i>«♡𝚁𝙷𝚈𝚃𝙷𝙼𝚁𝙾𝙲𝙺𝙴𝚁𝚉™♡»{file_name}</i>  </b> \n<b>│</b> \n<b>├⍟🗃𝑭𝒊𝒍𝒆 𝑺𝒊𝒛𝒆 : <code>{file_size}</code> </b> \n<b>│</b> \n<b>╰──[<a href=https://t.me/RhythmRockerz>❖ 𝑹𝒉𝒚𝒕𝒉𝒎 𝑹𝒐𝒄𝒌𝒆𝒓𝒛 ❖</a>]──⍟</b>')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '<b>╭──[𝑹𝑹_𝒓𝒆𝑸]───⧐</b> \n<b>│</b> \n<b>├⍟ 🗂 𝑭𝒊𝒍𝒆 𝑵𝒂𝒎𝒆 : <i>«♡𝚁𝙷𝚈𝚃𝙷𝙼𝚁𝙾𝙲𝙺𝙴𝚁𝚉™♡»{file_name}</i>  </b> \n<b>│</b> \n<b>├⍟🗃𝑭𝒊𝒍𝒆 𝑺𝒊𝒛𝒆 : <code>{file_size}</code> </b> \n<b>│</b> \n<b>╰──[<a href=https://t.me/RhythmRockerz>❖ 𝑹𝒉𝒚𝒕𝒉𝒎 𝑹𝒐𝒄𝒌𝒆𝒓𝒛 ❖</a>]──⍟</b>')
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎞 𝚃𝙸𝚃𝙻𝙴</b>: <a href={url}>{title}</a> <b> \n🎭 𝙶𝙴𝙽𝚁𝙴𝚂</b>: {genres} <b> \n🗓 𝚈𝙴𝙰𝚁</b>: <a href={url}/releaseinfo>{year}</a> <b> \n🌟 𝚁𝙰𝚃𝙸𝙽𝙶</b>: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.) <b> \n🎙 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴</b>: <code>{languages}</code> <b> \n📀 𝚁𝚄𝙽𝙽𝙸𝙽𝙶 𝚃𝙸𝙼𝙴</b>: {runtime} Minutes <b> \n📅 𝚁𝙴𝙻𝙴𝙰𝚂𝙴 𝙸𝙽𝙵𝙾</b>: {release_date} <b> \n📍 𝙲𝙾𝚄𝙽𝚃𝚁𝙸𝙴𝚂</b>: <code>{countries}</code> \n••••••••••••••••••••••••••••••••\n📚ʀᴇϙᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention} \n💚ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @RhythmRockerz \n••••••••••••••••••• \n<b>✎ɴᴏᴛᴇ : இதில் வரும் அனைத்தும் தமிழ் மட்டுமே😇</b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
