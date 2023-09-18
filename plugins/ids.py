import random
import re
from pyrogram import Client
from pyrogram.types import Message
from database import get_db_addcustomid, get_db_mypointgame, get_db_mymessage, get_db_mycontact
from localization import use_chat_lang
from config import get_bot_information
from plugins.admin import get_available_adminstrator
from plugins.rtp_function import get_Rank


def get_mycontact(m):
    if get_db_mycontact(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mycontact(m.from_user.id, m.chat.id)
    return num


def get_mypoint(m):
    if get_db_mypointgame(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mypointgame(m.from_user.id, m.chat.id)
    return num


def get_mymessage(m):
    if get_db_mymessage(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mymessage(m.from_user.id, m.chat.id)
    return num


def get_mymessage_interaction(m):
    interaction_msg = ''
    if m < 100:
        interaction_msg = 'ØºÙŠØ± Ù…ØªÙØ§Ø¹Ù„ ðŸ˜’'
    else:
        if m < 200:
            interaction_msg = 'Ù…ØªÙØ§Ø¹Ù„ Ø¶Ø¹ÙŠÙ ðŸ˜ž'
        else:
            if m < 400:
                interaction_msg = 'ØªÙØ§Ø¹Ù„Ùƒ Ø¶Ø¹ÙŠÙ Ù„ÙŠØ´ ðŸ˜•'
            else:
                if m < 700:
                    interaction_msg = 'ØªÙØ§Ø¹Ù„ Ù…ÙˆØ­Ù„Ùˆ ðŸ˜¤'
                else:
                    if m < 1200:
                        interaction_msg = 'Ø´Ø¨Ù‡ Ù…ØªÙØ§Ø¹Ù„ ðŸ™ŠðŸ¥º'
                    else:
                        if m < 2000:
                            interaction_msg = 'Ù…ØªÙØ§Ø¹Ù„ Ø¬Ø¯Ø§ ðŸ˜‚'
                        else:
                            if m < 3500:
                                interaction_msg = 'Ù…Ø¹Ø´Ø´ ÙÙ‰ Ø§Ù„Ø¬Ø±ÙˆØ¨ ðŸ”¥ðŸ˜¹'
                            else:
                                if m < 4000:
                                    interaction_msg = 'Ù…ØªÙØ§Ø¹Ù„ Ù†Ø§Ø± ðŸ”¥ðŸ˜'
                                else:
                                    if m < 4500:
                                        interaction_msg = 'Ù‚Ù…Ø© Ø§Ù„ØªÙØ§Ø¹Ù„ â˜ºï¸'
                                    else:
                                        if m < 5500:
                                            interaction_msg = 'Ù…Ù„Ùƒ Ø§Ù„ØªÙØ§Ø¹Ù„ ðŸ˜¼'
                                        else:
                                            if m < 7000:
                                                interaction_msg = 'Ù‚Ù†Ø¨Ù„Ù‡ ØªÙØ§Ø¹Ù„ ðŸŒŸ'
                                            else:
                                                if m < 9500:
                                                    interaction_msg = 'Ø§Ù…Ø¨Ø±ÙˆØ·ÙˆØ± Ø§Ù„ØªÙØ§Ø¹Ù„ ðŸ˜‰'
                                                else:
                                                    if m < 10000000000:
                                                        interaction_msg = 'ØªÙØ§Ø¹Ù„ Ù†Ø§Ø± ÙˆØ´Ø±Ø§Ø± ðŸ”¥ðŸ–¤'
    return interaction_msg


@use_chat_lang()
async def ids_private(c: Client, m: Message, strings):
    user_data = m.from_user
    await m.reply_text(strings("info_private").format(
                           first_name=user_data.first_name,
                           last_name=user_data.last_name or "",
                           username="@" + user_data.username if user_data.username else strings("none"),
                           user_id=user_data.id,
                           user_dc=user_data.dc_id or strings("unknown"),
                           lang=user_data.language_code or strings("unknown"),
                           chat_type=m.chat.type
                       ))


async def ids_default(c: Client, m: Message):
    randomtext = [
        'Ù…Ù„Ø§Ùƒ ÙˆØ¹Ø³Ù„ ÙŠØ§Ù†Ø§Ø³ ðŸ˜Ÿ',
        "Ø®Ø§ÙŠÙ Ø¹Ù„ÙŠÙƒ â˜¹ï¸ ",
        "Ø§Ø­Ø³Ù† ØµÙˆØ±Ù‡ ðŸ¼â¤ï¸",
        "ÙƒÙŠÙƒÙƒ ÙˆØ§Ù„Ù„Ù‡ðŸ¥º",
        "Ø¨Ø­Ø¨ Ù‡Ø§Ù‰ Ø§Ù„ØµÙˆØ±Ù‡ðŸ¥º",
        "ØºÙŠØ± Ù‡ÙŠÙ‰ Ø§Ù„ØµÙˆØ±Ù‡ Ø§Ù„Ø§Ù†ðŸ˜’",
        "Ø¨Ø·Ù„ Ù†ØªØ§Ù†Ù‡ Ø¨Ù‚Ø§Ù„Ùƒ ÙƒØ§Ù… Ø³Ù†Ù‡ Ø­Ø§Ø·Ø· Ø§Ù„ØµÙˆØ±Ù‡ Ø¯Ù‰ðŸ˜’"
    ]
    if m.reply_to_message:
        user_data = m.reply_to_message.from_user
        user_data2 = m.reply_to_message
    else:
        user_data = m.from_user
        user_data2 = m

    if user_data.first_name:
        first_name = user_data.first_name + " "
    else:
        first_name = " "
    if user_data.last_name:
        last_name = user_data.last_name
    else:
        last_name = ""

    if user_data.username:
        username = user_data.username
    else:
        username = "Ù„Ø§ÙŠÙˆØ¬Ø¯"

    check = await get_available_adminstrator(c, m)
    if check[0]:
        adminrom = "Ù…Ø´Ø±Ù"
    else:
        adminrom = "Ø¹Ø¶Ùˆ"

    medooid = f"""
Ø¹Ø°Ø±Ø§Ù‹ Ø¹Ø²ÙŠØ²ÙŠ Ø§Ù†Øª Ù„Ø§ ØªÙ…ØªÙ„Ùƒ ØµÙˆØ±Ø© Ø§Ùˆ Ø£Ù†Ùƒ Ù‚Ù…Øª Ø¨Ø­Ø¸Ø± Ø§Ù„Ø¨ÙˆØª Ø§Ø¶ØºØ· Ø§Ø³ØªØ§Ø±Øª [Ù‡Ù†Ø§](tg://user?id={get_bot_information()[0]}) ÙˆØªØ§ÙƒØ¯

ðŸ’Žâ•– Ø§ÙŠØ¯ÙÙŠÚª â‡‡ `{user_data.id}`
ðŸ£â•¢ Ø§Ø³Ù…Úª â‡‡ `{first_name + last_name}`
â˜€ï¸â•¢ ÙŠÙˆØ²Ø±Úª â‡‡ @{username}
ðŸŽˆâ•¢ Ù†Ù‚Ø§Ø·Ùƒ â‡‡ *{get_mypoint(m)}*
ðŸ’Œâ•¢ Ø±Ø³Ø§Ø¦Ù„Ùƒ â‡‡ *{get_mymessage(m)}*
ðŸ‘¥â•¢ Ø¬Ù‡Ø§ØªÙƒ â‡‡ *{get_mycontact(m)}*
ðŸ…â•¢ ØªÙØ§Ø¹Ù„Ùƒ â‡‡ {get_mymessage_interaction(get_mymessage(m))}
ðŸ‘®â€â™‚ï¸â•¢ Ø±ØªØ¨ØªÚª Ø¨Ø§Ù„Ø¨Ù€ÙˆØª â‡‡ {await get_Rank(user_data2)}
ðŸŒâ•¢ Ø±ØªØ¨ØªÚª Ø¨Ø§Ù„Ù€Ø±ÙˆÙ… â‡‡ {adminrom}
ðŸ’¬â•œ Ø±Ø³Ù€Ø§Ø¦Ù„ Ø§Ù„Ø¬Ù€Ø±Û†Ø¨ â‡‡ *{m.message_id + 1}*
        """

    medooid2 = f"""
{random.choice(randomtext)}
ðŸ’Žâ•– Ø§ÙŠØ¯ÙÙŠÚª â‡‡ `{user_data.id}`
ðŸ£â•¢ Ø§Ø³Ù…Úª â‡‡ `{first_name + last_name}`
â˜€ï¸â•¢ ÙŠÙˆØ²Ø±Úª â‡‡ @{username}
â­â•¢ Ù†Ù‚Ø§Ø·Ùƒ â‡‡ *{get_mypoint(m)}*
ðŸ’Œâ•¢ Ø±Ø³Ø§Ø¦Ù„Ùƒ â‡‡ *{get_mymessage(m)}*
ðŸ‘¥â•¢ Ø¬Ù‡Ø§ØªÙƒ â‡‡ *{get_mycontact(m)}*
ðŸ…â•¢ ØªÙØ§Ø¹Ù„Ùƒ â‡‡ {get_mymessage_interaction(get_mymessage(m))}
ðŸ‘®â€â™‚ï¸â•¢ Ø±ØªØ¨ØªÚª Ø¨Ø§Ù„Ø¨Ù€ÙˆØª â‡‡ {await get_Rank(user_data2)}
ðŸŒâ•¢ Ø±ØªØ¨ØªÚª Ø¨Ø§Ù„Ù€Ø±ÙˆÙ… â‡‡ {adminrom}
ðŸ’¬â•œ Ø±Ø³Ù€Ø§Ø¦Ù„ Ø§Ù„Ø¬Ù€Ø±Û†Ø¨ â‡‡ *{m.message_id + 1}*
            """

    elnagarid = f"""
ðŸ’Žâ•– Ø§ÙŠØ¯ÙÙŠÚª â‡‡ `{user_data.id}`
ðŸ£â•¢ Ø§Ø³Ù…Úª â‡‡ `{first_name + last_name}`
â˜€ï¸â•¢ ÙŠÙˆØ²Ø±Úª â‡‡ @{username}
â­â•¢ Ù†Ù‚Ø§Ø·Ùƒ â‡‡ *{get_mypoint(m)}*
ðŸ’Œâ•¢ Ø±Ø³Ø§Ø¦Ù„Ùƒ â‡‡ *{get_mymessage(m)}*
ðŸ‘¥â•¢ Ø¬Ù‡Ø§ØªÙƒ â‡‡ *{get_mycontact(m)}*
ðŸ…â•¢ ØªÙØ§Ø¹Ù„Ùƒ â‡‡ {get_mymessage_interaction(get_mymessage(m))}
ðŸ‘®â€â™‚ï¸â•¢ Ø±ØªØ¨ØªÚª Ø¨Ø§Ù„Ø¨Ù€ÙˆØª â‡‡ {await get_Rank(user_data2)}
ðŸŒâ•¢ Ø±ØªØ¨ØªÚª Ø¨Ø§Ù„Ù€Ø±ÙˆÙ… â‡‡ {adminrom}
ðŸ’¬â•œ Ø±Ø³Ù€Ø§Ø¦Ù„ Ø§Ù„Ø¬Ù€Ø±Û†Ø¨ â‡‡ *{m.message_id + 1}*
            """

    if not await c.get_profile_photos(user_data.id, limit=1):
        await m.reply_text(medooid, parse_mode="Markdown")

    async for photo in c.iter_profile_photos(user_data.id, limit=1):
        await m.reply_photo(photo.file_id, caption=medooid2, parse_mode="Markdown")


async def ids(c: Client, m: Message):
    if get_db_addcustomid(m.chat.id) is None:
        await ids_default(c, m)
    else:
        for per in get_db_addcustomid(m.chat.id):
            if per[1] == m.chat.id:
                randomtext = [
                    'Ù…Ù„Ø§Ùƒ ÙˆØ¹Ø³Ù„ ÙŠØ§Ù†Ø§Ø³ ðŸ˜Ÿ',
                    "Ø®Ø§ÙŠÙ Ø¹Ù„ÙŠÙƒ â˜¹ï¸ ",
                    "Ø§Ø­Ø³Ù† ØµÙˆØ±Ù‡ ðŸ¼â¤ï¸",
                    "ÙƒÙŠÙƒÙƒ ÙˆØ§Ù„Ù„Ù‡ðŸ¥º",
                    "Ø¨Ø­Ø¨ Ù‡Ø§Ù‰ Ø§Ù„ØµÙˆØ±Ù‡ðŸ¥º",
                    "ØºÙŠØ± Ù‡ÙŠÙ‰ Ø§Ù„ØµÙˆØ±Ù‡ Ø§Ù„Ø§Ù†ðŸ˜’",
                    "Ø¨Ø·Ù„ Ù†ØªØ§Ù†Ù‡ Ø¨Ù‚Ø§Ù„Ùƒ ÙƒØ§Ù… Ø³Ù†Ù‡ Ø­Ø§Ø·Ø· Ø§Ù„ØµÙˆØ±Ù‡ Ø¯Ù‰ðŸ˜’"
                ]
                if m.reply_to_message:
                    user_data = m.reply_to_message.from_user
                    user_data2 = m.reply_to_message
                else:
                    user_data = m.from_user
                    user_data2 = m

                if user_data.first_name:
                    first_name = user_data.first_name + " "
                else:
                    first_name = " "
                if user_data.last_name:
                    last_name = user_data.last_name
                else:
                    last_name = ""

                if user_data.username:
                    username = user_data.username
                else:
                    username = "Ù„Ø§ÙŠÙˆØ¬Ø¯"

                check = await get_available_adminstrator(c, m)
                if check[0]:
                    adminrom = "Ù…Ø´Ø±Ù"
                else:
                    adminrom = "Ø¹Ø¶Ùˆ"
                a = re.sub("#rdphoto", random.choice(randomtext), per[0])
                a = re.sub("#fname", str(first_name), a)
                a = re.sub("#lname", str(last_name), a)
                a = re.sub("#id", str(m.from_user.id), a)
                a = re.sub("#user", "@" + str(username), a)
                a = re.sub("#mention", f"[{first_name + last_name}](tg://user?id={m.from_user.id})", a)
                a = re.sub("#game", str(get_mypoint(m)), a)
                a = re.sub("#msgs", str(get_mymessage(m)), a)
                a = re.sub("#contact", str(get_mycontact(m)), a)
                a = re.sub("#auto", str(get_mymessage_interaction(get_mymessage(m))), a)
                a = re.sub("#brank", str(await get_Rank(user_data2)), a)
                a = re.sub("#grank", str(adminrom), a)
                a = re.sub("#gmsgs", str(m.message_id + 1), a)

                if not await c.get_profile_photos(user_data.id, limit=1):
                    await m.reply_text(a, parse_mode="Markdown")
                    return

                async for photo in c.iter_profile_photos(user_data.id, limit=1):
                    await m.reply_photo(photo.file_id, caption=a, parse_mode="Markdown")
                    return
        await ids_default(c, m)
