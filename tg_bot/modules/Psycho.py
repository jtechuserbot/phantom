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
    "ഞാൻ എന്താണോ പറഞ്ഞത് എന്നതിന് ഞാൻ ഉത്തരവാദിയാണ്.. പക്ഷെ.. നിങ്ങൾ എന്താണോ മനസിലാക്കിയത് എന്നുള്ളതിന് ഞാൻ ഉത്തരവാദിയല്ല 😌", 
    "മറക്കാനാവാത്ത വിധം ആഴത്തിൽ വേരിറക്കിയിരിക്കുന്നു നീ 😌", 
    "എന്നെ പറ്റി പരാതി പറയുന്നവരോട് എനിക്ക് ഒന്നേ പറയാനുള്ളു.. എനിക്ക് തന്നെ എന്നെപ്പറ്റി പരാതികളാണ്.. പിന്നെ എങ്ങനെ നിങ്ങൾക്ക് ഇല്ലാതിരിക്കും 😌", 
    "നിന്നിൽ നിന്ന് എന്നിലേക്ക് എനിക്ക് മടങ്ങുവാൻ നേരമായി.. വന്ന വഴിയിലൂടെ തിരിച്ചു പോവില്ല.. നീ വെട്ടിയ വഴിയിലൂടെ ഞാൻ മടങ്ങുന്നു.. 😌", 
    "അവരെന്തു കരുതും എന്ന കയറിൽ ആയിരുന്നു എന്റെ പല സന്തോഷങ്ങളും ആത്മഹത്യ ചെയ്തത്😌", 
    "മറ്റുള്ളവർ എന്നെ മനസ്സിലാക്കുന്നില്ലെന്നു അവരെ കുറ്റം പറയാൻ പറ്റില്ല.. കാരണം എന്റെ സ്വഭാവവും മനസ്സും എനിക്ക് തന്നെ പലപ്പോഴും മനസ്സിലാവുന്നില്ല.. 😌", 
    "ചില നേരം തോന്നും എന്നെ പോലെ പഞ്ചപാവം വേറെ ഇല്ലാന്ന്.. മറ്റുചിലപ്പോ എനിക്ക് എന്നെത്തന്നെ വെട്ടിക്കീറി അടുപ്പിൽ വെക്കാനും തോന്നും 😌", 
    
    )




@run_async
def psy(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(PSYCHO_STRINGS))
    else:
      message.reply_text(random.choice(PSYCHO_STRINGS))

__help__ = """
- /psy.
"""

__mod_name__ = "Psycho😌"

PSYCHO_HANDLER = DisableAbleCommandHandler("psy",psy)

dispatcher.add_handler(PSYCHO_HANDLER)
