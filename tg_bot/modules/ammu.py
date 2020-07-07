import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "പോടാ മരപ്പട്ടീ",
    "ഡാ കള്ളപ്പന്നീ",
    "ഡാ കോഴീ നിക്കെടാ അവിടേ..🤭🤭", 
    "നിന്നെകൊണ്ട് വല്ല്യ ശല്ല്യായല്ലോ..🤨🤨", 
    "ഒന്ന് പോയി തെരുവോ..😬😬", 
    "എന്നെ വളക്കാൻ മാത്രം വളർന്നോ നീ 😡😡", 
    "നിനക്കെന്നാഡാ  നിനക്കെന്തിന്റെ കേടാഡാ", 
    "നീ ഏതാടാ മരമാക്രീ", 
    "ചക്കരേന്നാ ആരുടെ ചക്കര കാൾ മീ അമ്മു", 
    "എന്തൊലിപ്പീരാഡേയ് 😏😏😏", 
    "പോടാ മാക്രിത്തലയാ",
    "ഡാ മങ്കി മാങ്ങാ തലയാ",
    "നീ പോടാ മങ്കി ഡോങ്കീ",
    "ഡാ കൊരങ്ങാ",
    "നീ പോടാ കാട്ടുകോഴി",
    "അമ്പട കള്ളാ 🤭🤭",
    "മ.. മ.. അല്ലേൽ അത് വേണ്ട.. മത്തങ്ങാതലയാ",
    "മാങ്ങാണ്ടി മോറാ",
    "എന്താ മോനൂസേ ജാടയാണോ?",
    "അത് നീ പള്ളീ പോയി പറഞ്ഞാ മതി",
    "നിന്റെ മണ്ടേലെന്താ കളിമണ്ണാണോ",
    "നിന്റെ ഉണ്ടക്കണ്ണു ഞാൻ കുത്തിപ്പൊട്ടിക്കും" 
  )

@run_async
def ammu(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /ammu  🤬.
"""

__mod_name__ = "ammu"

DARK_HANDLER = DisableAbleCommandHandler("ammu",ammu)

dispatcher.add_handler(DARK_HANDLER)
