import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

PWOLI_STRINGS = (
    "മുത്തുമണിയേ വളരെ നന്നായിട്ട്ണ്ട്ട്ടാ 🥰🥰", 
    "നീ അടിപൊളിയാണ് കിടു ആണ് കിക്കിടുവാണ് 👍",
    "മുത്തുമണി സൂപ്പർ ആണ് 😍😍", 
    "ആഹാ അടിപൊളി 😍😍👍", 
    "സൂപ്പർ 😍😍😍😍", 
    "പൊളിച്ചടുക്കി 😍😍😍👍", 
    "അൽ കിടു 😍😍👍", 
    "അമ്പമ്പോ പൊളി സാനം 😍😍👍",
    "ഇനിയും ഇതേ പോലുള്ള ഐറ്റംസ് പ്രതീക്ഷിക്കുന്നു 😍😍👍", 
    "എനിക്കറിയാർന്നു നീയിതു പൊളിച്ചടുക്കുമെന്നു 😍😍👍", 
    "മുത്തിന് ചേച്ചീടെ വക നൂറുമ്മകൾ 😘😘😘😘😘", 
  )

@run_async
def pwoli(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(PWOLI_STRINGS))
    else:
      message.reply_text(random.choice(PWOLI_STRINGS))

__help__ = """
- /pwoli👍.
"""

__mod_name__ = "Pwoli"

PWOLI_HANDLER = DisableAbleCommandHandler("pwoli",pwoli)

dispatcher.add_handler(PWOLI_HANDLER)
