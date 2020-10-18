import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

PSYCHO_STRINGS = (
    "മുത്തുമണിയേ വളരെ   നന്നായിട്ടണ്ട്ട്ടാ 🥰🥰", 
    "നീ അടിപൊളിയാണ് കിടു ആണ് കിക്കിടുവാണ് ", 
  )

@run_async
def psycho(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(PSYCHO_STRINGS))
    else:
      message.reply_text(random.choice(PSYCHO_STRINGS))

__help__ = """
- /psycho.
"""

__mod_name__ = "Psycho😌"

PSYCHO_HANDLER = DisableAbleCommandHandler("psycho",psycho)

dispatcher.add_handler(PSYCHO_HANDLER)