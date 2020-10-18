import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

PSYCHO_STRINGS = (
    "എങ്ങുമൊടുങ്ങാത്ത ജീവിതാസക്തികൾ തൂങ്ങി മരിച്ച വഴിയമ്പലങ്ങളിൽ കാര മുള്ളിന്റെ കിരീടവും ചൂടി നാം തേടി നടന്നത് സൗഖ്യമോ മൃത്യുവോ😌", 
    "സൈലന്റ് ആയിരിക്കുന്ന എന്നെ ചൊറിഞ്ഞു ചൊറിഞ്ഞു വയലന്റ് ആക്കിയിട്ടു സൈക്കോ എന്ന് വിളിക്കുന്നത് എന്തൊരു കഷ്ടമാണ് 😌 ", 
    "ഇതെന്റെ തലയ്ക്കു മീതെ തൂങ്ങിയാടുന്ന വാൾ... ചരടഴിഞ്ഞു മേൽ വീഴുന്ന നാൾ മോക്ഷം😌", 
    "പ്രാന്ത് പിടിച്ചാൽ പിന്നെ ആർക്കും ഒറ്റക്ക് ഇരിക്കേണ്ടി വരില്ല.. കൂട്ടിനു പ്രാന്തുണ്ടല്ലോ😌", 
    "ജീവിതത്തോളം രസമുള്ള ഗെയിം ഞാൻ ഒരു പ്ലേ സ്റ്റോറിലും കണ്ടിട്ടില്ല😌",
    "തീർത്തും സ്വന്തമെന്നു കരുതുന്ന ചിലതുണ്ട്.. ദൈവം, മനസ്സ്, സ്വന്തം ജീവൻ പിന്നെ നീ.. എവിടെ ഇരിക്കുന്നു എല്ലാം എന്നല്ലേ? കണ്ടിട്ടില്ല. കണ്ടിട്ടില്ലാത്തവയുമായുള്ള കൂട്ടുകെട്ടിന്റെ തിരക്കിൽ തന്നെ നാം ഇപ്പോഴും 😌", 
    "വെറുതെയല്ല വഴി തെറ്റി പോണത്.. ചെറുപ്പത്തിൽ വഴി തെറ്റിച്ചു വിട്ട ഉറുമ്പുകളുടെ ശാപം ഉണ്ടാവും 😌", 
    "പ്രതീക്ഷിക്കും തോറും പ്രതീക്ഷ നഷ്ടപ്പെടുന്നതിനെയാണോ സത്യത്തിൽ പ്രതീക്ഷകൾ എന്ന് വിളിക്കുന്നത്‌ 😌", 
    "ഓർക്കുക ആരുടെയൊക്കെയോ കഥകളിൽ നമ്മളും വില്ലന്മാരാണ് 😌",
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
