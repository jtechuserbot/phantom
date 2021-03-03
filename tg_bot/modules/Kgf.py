import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

KGF_STRINGS = (
      "അയിന് പോയി തല കുത്തി നിക്ക് 🤭🤭", 
      "അയിന് കുയിനെന്നു പറഞ്ഞു വന്നാൽ അടിച്ചു മണ്ട പൊളിക്കും ഞാൻ 😡😡", 
      "അയിന് അങ്ങട് മാറി നിക്ക് 🤭🤭", 
      "അയിന് പോയി തൂങ്ങി ചാവ് 🤭🤗",
      "അയിന് നീ ഏതാ 😡🤭",
      "അയിന് നല്ല അടി വെച്ച് തരും ഞാൻ 🤨🤨", 
)


@run_async
def kgf(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(KGF_STRINGS))
    else:
      message.reply_text(random.choice(KGF_STRINGS))

__help__ = """
- /kgf😌
"""

__mod_name__ = "kgf"

AYIN_HANDLER = DisableAbleCommandHandler("kgf",kgf)

dispatcher.add_handler(KGF_HANDLER)