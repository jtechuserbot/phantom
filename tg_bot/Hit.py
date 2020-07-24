import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

import tg_bot.modules.fun_strings as fun_strings
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user

HIT_JINN_TEMPLATES = (
    "ചേട്ടനെ ഞാൻ തല്ലില്ലാ 🥰🥰.",
    "ചേട്ടൻ എന്റെ മുത്താണ് 🥰🥰.",
    [
        "ചേട്ടാ സുഖല്ലേ 🥰🥰🥰🥰.",  # normal reply
        "ചേട്ടൻ സൂപ്പെറാ 🥰🥰😘😘.",  # reply to admin
        "tmute"  # command
    ]
)


HIT_TEMPLATES = (
   "ഡാ പരനാറി "
   "ഡാ പട്ടീ "
   "ഡാ വേട്ടാവളിയാ "
   )

@run_async
def hit(bot: Bot,update: Update, args: List[str]):
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == 1279942651:
        temp = random.choice(fun_strings.HIT_JINN_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(chat.id, message.from_user.id, until_date=mutetime, can_send_messages=False)
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(HIT_TEMPLATES)

    reply = temp.format(user1=user1, user2=user2)

    reply_text(reply, parse_mode=ParseMode.HTML)
