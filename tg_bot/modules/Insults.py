import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "{user} {victim}ന്റെ കണ്ണിൽ കാന്താരി മുളക് അരച്ച് തേച്ചു 😎😪.",
    "{user} {victim}ന്റെ തലക്ക് ഒലക്ക കൊണ്ട് അഞ്ചാറു അടി കൊടുത്തു 😪😪 .",
    "{user} ചാണകം വാരി {victim}ന്റെ മോന്തക്ക് എറിഞ്ഞു 🤢🤮 .",
    "{user} ഓടി വന്ന് {victim}ന്റെ തലയിൽ ചീമുട്ടയെറിഞ്ഞു 🤭🤭😜.",
    "{user} {victim}നെ കാലേ വാരി നിലത്തടിച്ചു 🤓☹️", 
    "{user} വലിയ പാറക്കല്ലെടുത്തു {victim}ന്റെ തലക്കെറിഞ്ഞു 😱😱🤭 .", 
    "{user} {victim}നെ വിളിച്ചോണ്ട് പോയി പൊട്ടകിണറ്റിൽ തള്ളിയിട്ടു 🤗🤗😝 .",
    "{user} കാക്കയെ വിളിച്ചു വരുത്തി {victim}ന്റെ തലയിൽ അപ്പിയിടീച്ചു 😝🤣 .",
    "{user} ഓടി വന്ന് ചൂരൽ കൊണ്ട് {victim}ന്റെ ചന്തിക്കിട്ട് അഞ്ചാറു അടി കൊടുത്ത് 😂😜 .",
    "{user} {victim}നെ കൊതുകിനെ കൊല്ലുന്ന പോലെ അടിച്ചു കൊന്നു 🤭😜.", 
    "{user} കോഴിക്കാഷ്ടം എടുത്ത് {victim}ന്റെ മുഖത്തു തേച്ചു 🤭🤣.", 
    "{user} {victim}ne എടുത്തോണ്ട് പോയി ചാണകക്കുഴിയിലിട്ടു 🤣🤣😛.", 
    "{user} പട്ടിയെ അഴിച്ചു വിട്ട് {victim}ന്റെ ചന്തിയിൽ കടിപ്പിച്ചു 😂😂😛.",
    "{user} കട്ടുറുറുമ്പിനെകൊണ്ട് {victim}ന്റെ കുണ്ടിക്ക് കടിപ്പിച്ചു 🤭🤭😜", 
    "{user} {victim}നെ കോഴിയാണെന്ന് കരുതി കൂട്ടിലടച്ചു 🤭🤭😜",
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
