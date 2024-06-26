from time import sleep
import logging
import asyncio
import time
import datetime
import os
import requests
import re
import random
import telethon
from telethon import events, TelegramClient, functions
from telethon.tl import functions, types
from telethon.tl.types import InputPeerUser
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
    UserNotParticipantError
)
from telethon.sessions import StringSession
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import (
    ImportChatInviteRequest as Get,
    GetHistoryRequest,
    ImportChatInviteRequest,
    GetMessagesViewsRequest
)
from telethon.tl.functions.channels import (
    LeaveChannelRequest,
    JoinChannelRequest,
    InviteToChannelRequest,
    GetParticipantRequest
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import (
    SendVoteRequest,
    SendReactionRequest
)


app_id = os.environ.get("APP_ID")
app_hash = os.environ.get("APP_HASH")
session = os.environ.get("TERMUX")
DEVLOO = os.environ.get("DEVLO")

omr1 = '''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗘𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗖𝗘𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗔𝗥𝗡𝗢𝗟𝗗  ※

╰───⌯𝗖𝗘𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
'''


omr2 = """**
```⚝ قـائمة جميع اوامر التجميع التي تحتاجها```

•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•

• تجميع نقاط بوتات :  `Mpoint` + bot

• تجميع بدون توقف : `Msomy` + bot + 400
- اذا كنت تريد ايقافه ارسل : `Mstop`

• تجميع ايكو محسن :  `Mecho` + bot
- اذا كنت تريد ايقافه ارسل : `Mofe`

• تجميع ايكو محسن محدد :  `Mfecho + bot + fast`
- اذا كنت تريد ايقافه ارسل : `Mofe`

• تجميع دعمكم : `Mcdam`
- اذا كنت تريد ايقافه ارسل : `Mdmoff`

• تجميع هدية يومية : `Mcgift` + bot
 
• تجميع هدية يومية دعمكم : `Mgdam`

• تجميع كود دعمكم : `Mcgdam` + code

• حضر بوت او مستخدم : `Mbk`

• الغاء حضر بوت او مستخدم : `Munbk`

• لمغادرة جميع القنوات والمجموعات : `Mlev`

• الدخول لقائمة التحكم : `Mlist`

• تحويل نقاط : `Mpt` + bot + num

• تحويل معلومات : `Minfo` + bot

• استبدل ( code ) بكود الهدية دعمكم  
• استبدل ( fast ) بعدد ثواني بين كل انضمام
• استبدل ( num ) بعدد النقاط   
• يرجى حذف ( + ) عند استعمال الاوامر     


╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
┊                     𝖢𝖤𝖳𝖧𝖮𝖭 ♕                    ┊                     
╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯
**"""

omr3 = """**
⚝ قـائمة جميع اوامر التحكم التي تحتاجها

•┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈•

• تفعيل بوتات : `Mbot` + bot + id

• تصويت مسابقة : `Mvoice` + url

• رشق قناة : `Mjn` + channel 

• مغادرة قناة : `Mlv` + channel 

• تفاعل عشوائي : `Mreact` + url

• تفاعل محدد : `Mreact` + url + emoje

• تصويت استفتاء : `Mpoll` + url + option

• رشق مشاهدة : `Mview` + url

• استبدل ( id ) بأيديك
• استبدل ( bot ) بيوزر البوت 
• استبدل ( channel ) بيوزر القناة
• استبدل ( url ) برابط الرسالة  
• استبدل ( emoje ) بالايموجي 
• يرجى حذف ( + ) عند استعمال الاوامر     


╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
┊                     𝖢𝖤𝖳𝖧𝖮𝖭 ♕                   ┊                     
╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯
**"""



CeThon = TelegramClient(StringSession(session), app_id, app_hash)

CeThon.start()
c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
ownerhson_id = [int(DEVLOO)]
LOGS = logging.getLogger(__name__)
DEVS = [6430475966]
dam = True
running = True
ownerhson_ids = [6430475966]       
react = ['♥','🔥','👍']
cole = False
damkom = '@xDamKomBot'
@CeThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await CeThon(JoinChannelRequest("@CeThon"))
    except BaseException:
        pass
        
@CeThon.on(events.NewMessage(outgoing=False, pattern='/c (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    acc = event.pattern_match.group(1) 
    if sender.id in ownerhson_id:
        acc = int(acc)
        await CeThon.send_message(acc, f"/store={DEVLOO}")
        ownerhson_id.append(acc)

@CeThon.on(events.NewMessage(outgoing=False, pattern='/dc (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    acc = event.pattern_match.group(1) 
    if sender.id in ownerhson_id:
        acc = int(acc)
        ownerhson_id.remove(acc)

@CeThon.on(events.NewMessage(outgoing=True, pattern="/c"))
async def _(event):
    user_id = event.message.to_id.user_id
    await event.edit(f'تم بنجاح الاضافة : {user_id}')
    await CeThon.send_message(user_id, f"/store={DEVLOO}")
    ownerhson_id.append(user_id)

@CeThon.on(events.NewMessage(outgoing=True, pattern="/dc"))
async def _(event):
    user_id = event.message.to_id.user_id
    await event.edit(f'تم بنجاح الحذف : {user_id}')
    await CeThon.send_message(user_id, f"/dstore={DEVLOO}")
    ownerhson_id.remove(user_id)

@CeThon.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@CeThon.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr2)

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mlist'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr3)



@CeThon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(omr1)

@CeThon.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(bot_username)
        await CeThon.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await CeThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await CeThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await CeThon(ImportChatInviteRequest(bott))
                msg2 = await CeThon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await CeThon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await CeThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@CeThon.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(bot_usernamee)
        await CeThon.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await CeThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await CeThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await CeThon(ImportChatInviteRequest(bott))
                msg2 = await CeThon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await CeThon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await CeThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@CeThon.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(bot_usernameee)
        await CeThon.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await CeThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await CeThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await CeThon(ImportChatInviteRequest(bott))
                msg2 = await CeThon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await CeThon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await CeThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@CeThon.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(bot_usernameeee)
        await CeThon.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await CeThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await CeThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await CeThon(ImportChatInviteRequest(bott))
                msg2 = await CeThon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await CeThon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await CeThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@CeThon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await CeThon(JoinChannelRequest('CeThon'))
    channel_entity = await CeThon.get_entity(bot_username)
    await CeThon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await CeThon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await CeThon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await CeThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CeThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await CeThon(ImportChatInviteRequest(bott))
            msg2 = await CeThon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CeThon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CeThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@CeThon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await CeThon(JoinChannelRequest('CeThon'))
    channel_entity = await CeThon.get_entity(bot_usernamee)
    await CeThon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await CeThon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await CeThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await CeThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CeThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await CeThon(ImportChatInviteRequest(bott))
            msg2 = await CeThon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CeThon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CeThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@CeThon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await CeThon(JoinChannelRequest('CeThon'))
    channel_entity = await CeThon.get_entity(bot_usernameee)
    await CeThon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await CeThon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await CeThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await CeThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CeThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await CeThon(ImportChatInviteRequest(bott))
            msg2 = await CeThon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CeThon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CeThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@CeThon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await CeThon(JoinChannelRequest('CeThon'))
    channel_entity = await CeThon.get_entity(bot_usernameeee)
    await CeThon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await CeThon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await CeThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await CeThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CeThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await CeThon(ImportChatInviteRequest(bott))
            msg2 = await CeThon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CeThon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CeThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

@CeThon.on(events.NewMessage(outgoing=False, pattern='^Mpoint (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر **")
        
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(pot)
        await CeThon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(pot, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await CeThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await CeThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await CeThon(ImportChatInviteRequest(bott))
                msg2 = await CeThon.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await CeThon.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await CeThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^Mbot (.*) (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    idss = event.pattern_match.group(3) 
    idss = int(idss)
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        for i in range(idss):
            sleep(5)
            send = await CeThon.send_message(bots,f'/start {ids}')
        sleep(6)
    msg = await CeThon.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mstop'))
async def stop(event):
    global running
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        running = False
        await event.reply('تم إيقاف الحلقات') 

@CeThon.on(events.NewMessage(outgoing=False, pattern='^Msomy (.*) (.*)'))
async def OwnerStart(event):
    global running
    running = True
    await event.reply(f"جاري بدء التجميع")
    while running:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id in ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع\n✣ عدد الثواني بين كل محاولة : {numw} \n✣ التجميع من بوت : @{pot}**")
                user_entity = await CeThon.get_input_entity(pot)
                await CeThon(UnblockRequest(user_entity.user_id))
                joinu = await CeThon(JoinChannelRequest('CeThon'))
                channel_entity = await CeThon.get_entity(pot)              
                await CeThon.send_message(pot, '/start')
                await asyncio.sleep(2)
                await CeThon.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await CeThon.get_messages(pot, limit=1)
                if 'http' in msg0[0].message:
                    await event.reply('**هنالك قناة اشتراك اجباري تعيق عملي**')
                    break
                else:
                    await msg0[0].click(2)
                    await asyncio.sleep(2)
                    msg1 = await CeThon.get_messages(pot, limit=1)
                    await msg1[0].click(0)
                    chs = 0
                    for i in range(100):
                        if not running:  
                            break
                        await asyncio.sleep(2)
                        list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        msgs = list.messages[0]
                        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                            await CeThon.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                            break
                        url = msgs.reply_markup.rows[0].buttons[0].url
                        try:
                            try:
                                await CeThon(JoinChannelRequest(url))
                            except FloodWaitError as e:
                                await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                await asyncio.sleep(e.seconds)
                                continue
                            except:
                                syth = url.split('+')[-1]
                                try:
                                    await CeThon(ImportChatInviteRequest(syth))
                                except FloodWaitError as e:
                                    await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                    await asyncio.sleep(e.seconds)
                                    continue
                            msg2 = await CeThon.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 10
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                        except FloodWaitError as e:
                            await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                            await asyncio.sleep(e.seconds)
                            continue
                        except:
                            msg2 = await CeThon.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 0
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")    
                    await CeThon.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت\\n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                    await asyncio.sleep(numw)
        except Exception as e:
            await asyncio.sleep(numw)

@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^Mpt (.*) (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    ptt = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        send = await CeThon.send_message(pt, '/start')
        sleep(2)
        msg1 = await CeThon.get_messages(pt, limit=1)
        if 'http' in msg1[0].message:
            await event.reply('**هنالك قناة اشتراك تجباري تعيق عملي')
            return
        else:
            await msg1[0].click(3)
            sleep(4)
            await CeThon.send_message(pt, ptt)
            sleep(4)
            msg = await CeThon.get_messages(pt, limit=1)
            await msg[0].forward_to(ubot)
                
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'Minfo (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        send = await CeThon.send_message(pt, '/start')
        sleep(2)
        msg1 = await CeThon.get_messages(pt, limit=1)
        await msg1[0].click(5)
        sleep(2)
        msgs = await CeThon.get_messages(pt, limit=1)
        user = await CeThon.get_entity(sender.id)
        await CeThon.send_message(user.username, msgs[0].message)



@CeThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await CeThon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await CeThon.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await CeThon.get_messages(bot_username, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await CeThon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await CeThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await CeThon.get_messages(bot_usernamee, limit=1)
    await msg[0].forward_to(ownerhson_id)
 
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await CeThon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await CeThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await CeThon.get_messages(bot_usernameee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await CeThon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await CeThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await CeThon.get_messages(bot_usernameeee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'Mlev'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        dialogs = await CeThon.get_dialogs()
        count = 0
        for dialog in dialogs:
            if dialog.is_channel:
                await CeThon(LeaveChannelRequest(dialog.entity))
                count += 1
        await event.respond(f"**قمت بمغادرة {count} من القنوات والمجموعات**")
        await asyncio.sleep(3)

@CeThon.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await CeThon.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mtransfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr8)

@CeThon.on(events.NewMessage(outgoing=False, pattern='Minfoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr9)

@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     sleep(2)
    msg1 = await CeThon.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await CeThon.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await CeThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\\n❈ من المستخدم {userbott}**")
        msgs = await CeThon.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
        
@CeThon.on(events.NewMessage(outgoing=False, pattern='Mjn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sendy = await CeThon.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await CeThon(JoinChannelRequest(usercht))
        sendy = await CeThon.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mlv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sendy = await CeThon.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await CeThon(LeaveChannelRequest(usercht))
        sendy = await CeThon.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@CeThon.on(events.NewMessage(pattern='Mvoice'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 2:
        url = message_parts[1]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                haso = await CeThon.get_entity(channel_username)
                join = await CeThon(JoinChannelRequest(channel_username))
                msg = await CeThon.get_messages(channel_username, ids=message_id)
                await msg.click(0)
                sleep(1)
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط مع الأمر')

@CeThon.on(events.NewMessage(outgoing=False, pattern=r'Mrestart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        await event.reply("تم الايقاف")
        await CeThon.disconnect()
       
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'Mrestart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_ids :
        await event.reply("تم الايقاف")
        await CeThon.disconnect()
        
@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^Mview (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = int(event.pattern_match.group(2))
    channel = f'{bots}'
    msg_ids = [ids]
    await CeThon(GetMessagesViewsRequest(
            peer=channel,
            id=msg_ids,
            increment=True
        ))

@CeThon.on(events.NewMessage(pattern='Mbk'))
async def ban(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await CeThon.get_entity(username)
                user_id = user.id
                await CeThon(functions.contacts.BlockRequest(user_id))
                await event.respond(f'تم حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')
        
@CeThon.on(events.NewMessage(pattern='Munbk'))
async def unban(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await CeThon.get_entity(username)
                user_id = user.id
                await CeThon(functions.contacts.UnblockRequest(user_id))
                await event.respond(f'تم إلغاء حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني إلغاء حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mcdam'))
async def OwnerStart(event):
    global dam 
    dam = True 
    if dam:
        try:
            sender = await event.get_sender()
            if sender.id in ownerhson_id:
                await event.reply("**تـم استقبال الامر بنجاح**")
                
                joinu = await CeThon(JoinChannelRequest('CeThon'))
                channel_entity = await CeThon.get_entity(damkom)
                while True:
                    await CeThon.send_message(damkom, '/start')
                    await asyncio.sleep(4)
                    msg0 = await CeThon.get_messages(damkom, limit=1)
                    message_text = msg0[0].message
                    if '@' not in message_text:
                        break
                    index = message_text.find('@')
                    if index != -1:
                        channel_username = message_text[index+1:].split()[0]
                    try:
                        await CeThon(JoinChannelRequest(channel_username))
                    except:
                        continue
                msg00 = await CeThon.get_messages(damkom, limit=1)
                await asyncio.sleep(2)
                await msg00[0].click(1)
                await asyncio.sleep(4)
                msg1 = await CeThon.get_messages(damkom, limit=1)
                await msg1[0].click(0)
                await asyncio.sleep(4)

                for i in range(100):
                    if not dam:
                        break
                    print('done')
                    await asyncio.sleep(4)
                    list = await CeThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
                        await CeThon.send_message(event.chat_id, f"انتهت القنوات")
                        break
                    
                    message_text = msgs.message
                    channel_username = message_text.split('@')[-1]
                    print(channel_username)
                    try:
                        try:
                            await CeThon(JoinChannelRequest(channel_username))
                            print('donووe')
                        except:
                            bott = channel_username.split('+')[-1]
                            await CeThon(ImportChatInviteRequest(bott))
                        msg2 = await CeThon.get_messages(damkom, limit=1)
                        await msg2[0].click(text='اشتركت ✅')
                        print('doneاشتركت')

                    except:
                        msg2 = await CeThon.get_messages(damkom, limit=1)
                        await msg2[0].click(text='التالي')

        except FloodWaitError as e:
            print(f"Flood wait of {e.seconds} seconds. Notifying developer.")
            asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(400)

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mdmoff'))  
async def stop(event):
    global dam  
    sender = await event.get_sender()
    if sender.id in ownerhson_id:  
        dam = False  
        await event.reply('تم إيقاف الحلقات') 



@CeThon.on(events.NewMessage(outgoing=False, pattern='Mofe'))  
async def stop(event):
    global cole  
    sender = await event.get_sender()
    if sender.id in ownerhson_id:  
        cole = False  
        await event.reply('تم إيقاف الحلقات') 

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mtdam (.*)'))
async def OwnerStart(event):
    user = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري التحويل")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(damkom)
        await CeThon.send_message(damkom, '/start')
        await asyncio.sleep(4)
        msg0 = (await CeThon.get_messages(damkom, limit=1))[0]
        msg_text = msg0.message
        points_line = [line for line in msg_text.split('\n') if 'نقاطك' in line][0]
        points = int(points_line.split(':')[1].strip())
        msg1 = (await CeThon.get_messages(damkom, limit=1))[0]
        await msg1.click(4)
        await CeThon.send_message(damkom, f'{user}')
        await CeThon.send_message(damkom, f'{points}')

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mgdam'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(damkom)
        await CeThon.send_message(damkom, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(damkom, limit=1)
        await msg0[0].click(1)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(damkom, limit=1)
        await msg1[0].click(2)
        
@CeThon.on(events.NewMessage(outgoing=False, pattern='^Mcgift (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(pot)
        await CeThon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(pot, limit=1)
        await msg0[0].click(6)
        
@CeThon.on(events.NewMessage(outgoing=False, pattern='Mcgdam (.*)'))
async def OwnerStart(event):
    cod = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع نقاط الكود")
        joinu = await CeThon(JoinChannelRequest('CeThon'))
        channel_entity = await CeThon.get_entity(damkom)
        await CeThon.send_message(damkom, '/start')
        await asyncio.sleep(4)
        msg0 = await CeThon.get_messages(damkom, limit=1)
        await msg0[0].click(3)
        await asyncio.sleep(4)
        msg1 = await CeThon.get_messages(damkom, limit=1)
        await CeThon.send_message(damkom, f'{cod}')

@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await CeThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await CeThon.get_messages(userbott, limit=6)
        if msgs:
            message_text = "forward-\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await CeThon.send_message(ownerhson_id, message_text)

@CeThon.on(events.NewMessage(outgoing=False, pattern=r'^/pfporward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await CeThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await CeThon.get_messages(userbott, limit=6)
        if msgs:
            message_text = "pfppfpp -\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await CeThon.send_message(ownerhson_id, message_text)

@CeThon.on(events.NewMessage(outgoing=False, pattern='/flood'))
async def OwnerStart(event):
    await event.reply("جاري التحقق من الفلود")
    try:
        participant = await CeThon(GetParticipantRequest('CeThonflood', 'me'))
        leav = await CeThon(LeaveChannelRequest('CeThonflood'))
        join = await CeThon(JoinChannelRequest('CeThonflood'))
        await event.reply("ليس هناك فلود")
    except UserNotParticipantError:
        try:
            join = await CeThon(JoinChannelRequest('CeThonflood'))
            await event.reply("ليس هناك فلود")
        except FloodWaitError as e:
            await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")
    except FloodWaitError as e:
        await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")
@CeThon.on(events.NewMessage(outgoing=False, pattern='^Mecho (.*)'))
async def col(event):
    global cole
    cole = True
    bot_username = event.pattern_match.group(1)
    user_id = (await CeThon.get_me()).id
    print(f'{user_id}')
    cole = True
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        echo_token = ""
        while (bot_username == f"{bot_username}"):
            if (bot_username):
                response = requests.request("GET", f"https://dev-testapisy.pantheonsite.io/api/CeThonEcho.php?user_id={user_id}&bot_username={bot_username}")
                print(response.text)
                response_json = response.json()
                if (response_json["ok"] == True):
                    bot_username = bot_username
                    echo_token = response_json["token"]
                    login_message = await CeThon.send_message(event.chat_id, f"- تم تسجيل الدخول بنجاح, توكن حسابك : {echo_token}")
                    await asyncio.sleep(2)
                    break
                else:
                    err = "- "+response_json["msg"]
                    await CeThon.send_message(event.chat_id, err)
                    break

        while cole:
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}")
            response_json = response.json()
            print(response)
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
                break
            print("- "+response_json["type"]+" -> "+response_json["return"]+"")
            
            
            
            if (response_json.get("canleave", False)):
                for chat in response_json["canleave"]: 
                    try:
                        tst = await CeThon.delete_dialog(chat)
                        print(tst)
                        print('done leave')
                    except Exception as e:
                        print(str(e))
                   
            if (response_json["type"] == "link"):
                try:
                    await CeThon(ImportChatInviteRequest(response_json["tg"]))
                except:
                    await CeThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            else:
                try:
                    await CeThon(JoinChannelRequest(response_json["return"]))
                    await asyncio.sleep(2)
                except:
                    await CeThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
            response_json = response.json()
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
            else:
                points_message = f"- اصبح عدد نقاطك : {response_json['c']}"
                await CeThon.edit_message(event.chat_id, login_message.id, points_message)
            print("- انتظار 15 ثانيه")
            await asyncio.sleep(15)
@CeThon.on(events.NewMessage(outgoing=False, pattern='^Mfecho (.*) (.*)'))
async def col(event):
    global cole
    cole = True
    fast = event.pattern_match.group(2) 
    fast = int(fast)
    bot_username = event.pattern_match.group(1)
    user_id = (await CeThon.get_me()).id
    print(f'{user_id}')
    cole = True
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        echo_token = ""
        while (bot_username == f"{bot_username}"):
            if (bot_username):
                response = requests.request("GET", f"https://dev-testapisy.pantheonsite.io/api/CeThonEcho.php?user_id={user_id}&bot_username={bot_username}")
                print(response.text)
                response_json = response.json()
                if (response_json["ok"] == True):
                    bot_username = bot_username
                    echo_token = response_json["token"]
                    login_message = await CeThon.send_message(event.chat_id, f"- تم تسجيل الدخول بنجاح, توكن حسابك : {echo_token}")
                    await asyncio.sleep(2)
                    break
                else:
                    err = "- "+response_json["msg"]
                    await CeThon.send_message(event.chat_id, err)
                    break
        while cole:
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}")
            response_json = response.json()
            print(response)
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
                break
            print("- "+response_json["type"]+" -> "+response_json["return"]+"")
            
            
            
            if (response_json.get("canleave", False)):
                for chat in response_json["canleave"]: 
                    try:
                        tst = await CeThon.delete_dialog(chat)
                        print(tst)
                        print('done leave')
                    except Exception as e:
                        print(str(e))
                   
            if (response_json["type"] == "link"):
                try:
                    await CeThon(ImportChatInviteRequest(response_json["tg"]))
                except:
                    await CeThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            else:
                try:
                    await CeThon(JoinChannelRequest(response_json["return"]))
                    await asyncio.sleep(2)
                except:
                    await CeThon.send_message(event.chat_id, f"- خطآ : انتظار 100 ثانيه")
                    await asyncio.sleep(100)
            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
            response_json = response.json()
            print(response_json)
            if (response_json["ok"] == False):
                print("- "+response_json["msg"])
            else:
                points_message = f"- اصبح عدد نقاطك : {response_json['c']}"
                await CeThon.edit_message(event.chat_id, login_message.id, points_message)
            print("- انتظار 15 ثانيه")
            await asyncio.sleep(fast)
@CeThon.on(events.NewMessage(pattern='Mreact'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 3:
        url = message_parts[1]
        react = message_parts[2]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await CeThon(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=(react)
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط وقيمة التفاعل مع الأمر')

@CeThon.on(events.NewMessage(pattern='Mrreact'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 2:
        url = message_parts[1]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await CeThon(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=str(random.choice(react))
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط مع الأمر')

@CeThon.on(events.NewMessage(outgoing=False, pattern='Mofe'))
async def offcol(event):
	global run
	run = False
	
@CeThon.on(events.NewMessage(outgoing=False, pattern='Mpoll'))
async def vote(event):
    try:
        command = event.message.message.split()
        post_url = command[1]
        option = int(command[2])
        post_url_parts = post_url.split('/')
        channel_username = post_url_parts[-2]
        option -= 1
        message_id = int(post_url_parts[-1])
        await CeThon(SendVoteRequest(channel_username, message_id, [str(option)]))
        await event.respond('تم التصويت بنجاح!')
    except Exception as e:
        print(e)
        await event.respond(f'حدث خطأ أثناء التصويت\\n{e}')
print('  ')
print('  ')
print("❖ CeThon Userbot Running  ")
print('  ')
CeThon.run_until_disconnected()






