import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

AYIN_STRINGS = (
      "https://telegra.ph/file/76c095429d6371f4417bb.jpg", 
      "https://telegra.ph/file/67e3b184e2337a30e409d.jpg", 
      "https://telegra.ph/file/124c3947ce23efe4ab689.jpg", 
      "https://telegra.ph/file/a39ebd40748ac79a20db2.jpg", 
)
@run_async
def ayin(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(AYIN_STRINGS))
    else:
      message.reply_text(random.choice(AYIN_STRINGS))

__help__ = """
- /ayin.
"""

__mod_name__ = "Ayin"

AYIN_HANDLER = DisableAbleCommandHandler("ayin",ayin)

dispatcher.add_handler(AYIN_HANDLER)
