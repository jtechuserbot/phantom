import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

KOZHI_STRINGS = (
    "എടാ കള്ളക്കോയീ 🐓🐓😂😂😂",
    "കോയീ  ചിങ്കാര പൂങ്കോയീ...🎶🎶😜 ",
    "ഡാ കോഴീ നിക്കെടാ അവിടേ..🤭🤭", 
    "ബ  ബ്ബാ ബ്ബാ ബ്ബാ കോയീ ബാ ബാ ..🤨🤨", 
    "കോയികുഞ്ഞേ നിന്റെ പാട്ടൊന്നു കേക്കട്ടെ ഞാനും ചെറുപ്പത്തിൽ കീയോ കീയോ 🎶 😜😬😬", 
    "ശ്ശോ പോ കോയീ.....🐓🐓 ",
    "നിന്നെ കണ്ടപ്പൊഴാ ഒരു കാര്യം ഓർത്തേ ഇന്ന് കോയിക്ക് തീറ്റ കൊടുത്തില്ല 😌😌😌🥺",  
    "പോയി  കൂട്ടിൽ കേറ് കോഴിയേ.... 😛😛😜", 
    "നിന്റെ കുണുങ്ങി കുണുങ്ങി ഉള്ള വരവ് കണ്ടാലേ അറിയാം നല്ല ഒന്നാന്തരം കാട്ടുകോഴിയാണെന്ന് 🐓😎 ", 
    "കോയീ വാവാവോ എന്റെ കോയീ വാവാവോ 😂😂😂", 
    "എന്തൊലിപ്പീരാഡേയ് 😏😏😏", 
    "നീ പോടാ കാട്ടുകോഴീ 🐓🐓", 
    "കുണുക്കിട്ട കോഴീ കുളക്കോഴീ...🎶 😂😂😜", 
  )

@run_async
def kozhi(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(KOZHI_STRINGS))
    else:
      message.reply_text(random.choice(KOZHI_STRINGS))

__help__ = """
- /kozhi 🐓.
"""

__mod_name__ = "Kozhi"

KOZHI_HANDLER = DisableAbleCommandHandler("kozhi",kozhi)

dispatcher.add_handler(KOZHI_HANDLER)
