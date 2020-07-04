import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "ഡാ ചൊറിത്തവളേ ",
    "നീ പോടാ മരമാക്രീ 😡😡🤬", 
    "വാടാ മരപ്പട്ടീ 😡😡", 
    "എന്താടാ നിന്റെ നാവിറങ്ങിപ്പോയാ 😡😡", 
    "ധൈര്യണ്ടേൽ മുട്ടാൻ വാടാ.. 😡😡", 
    "അടിച്ചു നിന്റെ മണ്ട പൊളിക്കും ഞാൻ ", 
    "അടിച്ചു നിന്റെ മുപ്പത്തിരണ്ട് പല്ലും ഞാൻ കൊഴിക്കും ", 
    "തരത്തിൽ പോയി കളിക്കെടാ ചെക്കാ 😡😡", 
    "എന്താടാ നിന്റെ മുട്ട് വിറക്കുന്നുണ്ടോ 😡😡", 
    "ഇനി ഇമ്മാതിരി കോഴിത്തരോം കൊണ്ട് ഇവിടെ വന്നാൽ പൊന്നുമോനെ ഭിത്തിയേന്ന് വടിച്ചെടുക്കേണ്ടി വരും നിന്നെ..", 
)

@run_async
def insult(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- Reply to a text with /insult for insults.
"""

__mod_name__ = "Insults"

INSULT_HANDLER = DisableAbleCommandHandler("insult", insult)

dispatcher.add_handler(INSULT_HANDLER)
