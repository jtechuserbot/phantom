import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "പോടാ മരപ്പട്ടീ",
    "ഡാ കള്ളപ്പന്നീ",
    "പുന്നാര മോനെ",
    "പോടാ മാക്രിത്തലയാ",
    "ഡാ മങ്കി മാങ്ങാ തലയാ",
    "വാടാ ... വവ്വാലേ",
    "പോയി ചാവടാ കൊരങ്ങാ",
    "നീ പോടാ കാട്ടുകോഴി",
    "പോയി ചത്തൂടെ നിനക്ക്",
    "കോപ്പേ വല്യ ബഹളം വേണ്ട",
    "മ.. മ.. അല്ലേൽ അത് വേണ്ട.. മത്തങ്ങാതലയാ",
    "മാങ്ങാണ്ടി മോറാ",
    "ഡാ പന്നക്കിളവാ",
    "അത് നീ പള്ളീ പോയി പറഞ്ഞാ മതി",
    "നിന്റെ മണ്ടേലെന്താ കളിമണ്ണാണോ",
    "നിന്റെ ഉണ്ടക്കണ്ണു ഞാൻ കുത്തിപ്പൊട്ടിക്കും" 
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /dark  🤬.
"""

__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)
