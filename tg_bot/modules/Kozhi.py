import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

KOZHI_STRINGS = (
    "എടാ കള്ളക്കോയീ 🐓🐓😂😂😂",
    "കോയീ  ചിങ്കാര പൂങ്കോയീ...🎶🎶😜 ",
    "എടാ കോഴിക്കുട്ടാ നിനക്ക് ഇത് തന്ന്യാ പരിപാടി 😂😂🤭🤭",
    "ഡാ കോഴീ നിക്കെടാ അവിടേ..🤭🤭", 
    "ബ  ബ്ബാ ബ്ബാ ബ്ബാ കോയീ ബാ ബാ ..🤨🤨",
    "കോഴികളിലെ കാട്ടുകോഴി തല മൂത്ത തള്ളക്കോഴി കോഴിത്തലയൻ രാജാവ് എഴുന്നള്ളുന്നേ 😂😂🤭🤭", 
    "കോയികുഞ്ഞേ നിന്റെ പാട്ടൊന്നു കേക്കട്ടെ ഞാനും ചെറുപ്പത്തിൽ കീയോ കീയോ 🎶 😜😬😬", 
    "ശ്ശോ പോ കോയീ.....🐓🐓 ",
    "നിന്നെ കണ്ടപ്പൊഴാ ഒരു കാര്യം ഓർത്തേ ഇന്ന് കോയിക്ക് തീറ്റ കൊടുത്തില്ല 😌😌😌🥺",  
    "പോയി  കൂട്ടിൽ കേറ് കോഴിയേ.... 😛😛😜", 
    "ഗാംഗുമായി വരുന്നവൻ റൂസ്റ്റർ അവൻ വന്നത് ഒറ്റക്കായിരുന്നു.... ---വൈൽഡ് റൂസ്റ്റർ 😌😌🤭🤭",  
    "കോയീ വാവാവോ എന്റെ കോയീ വാവാവോ 😂😂😂", 
    "എചുശ്മി ഏത് കൂട്ടിലെ കോഴിയാ? 😌😌🤭", 
    "നീ പോടാ കാട്ടുകോഴീ 🐓🐓", 
    "കുണുക്കിട്ട കോഴീ കുളക്കോഴീ...🎶 😂😂😜",
    "അവന്റെ കൂവൽ കേട്ട് പ്രപഞ്ചം പോലും വിറങ്ങലിച്ചു നിന്നു 😌😌🤭🤭",
    "ഒന്ന് ചുമ്മായിരിക്ക് കോഴ്യെ 😌😌🤭🤭 ",
    "ആരേലും ഈ കോഴിക്കിച്ചിരി തീറ്റി ഇട്ടു കൊടുത്തേ 😌😌🤭🤭",
    "എന്തോന്നടെയ് കോഴിത്തരത്തിനൊക്കെ ഒരു പരിധിയില്ലേ 😌😌🤭🤭",
    "ഓഹ് മൈ ഗോഡ് ബ്ലഡി കോഴിക്കൂട് വാസീസ് 🙄🙄😜",
    "ഹേയ് മിസ്റ്റർ കോഴി എനിക്ക് താങ്കളെ മനസ്സിലാവുന്നില്ല 🥺🥺😜",
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
