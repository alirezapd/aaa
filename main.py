from pyrogram.client import Client, Filters
from pyrogram.errors import FloodWait
from time import sleep

session_name, api_id, api_hash = "pyrobot", 538848, "24416a50579e542238769a509be70ce7"
bot = Client( session_name=session_name, api_id=api_id, api_hash=api_hash )

admin = [175770489, 769961309]

bot_list = [
    'alirezabot', 'voocabot', 'trello_bot', 'RavenApiBot', 'EvinSupBot',
    'RexerRobot', 'AlirezaSupBot', 'PandaRpbot', 'WikimaBot', 'GpyNanoBot', # 10
    'kamranbot', 'makerbot', 'youtubebot', 'mohammadbot', 'kavehbot',
    'alibot', 'samanbot', 'heidarbot', 'abbasbot', 'sholexbot', # 20
    'tdlibevinbot', 'ahmadbot', 'hajirobot', 'xonerobotmypertelethonbot', 'nothinggzjbot',
    'khazaeliversion4bot', 'feewdxbot', 'techbot', 'booksbot', 'pythonbot', # 30
    'gifinderbot', 'redken_bot', 'guggybot', 'updat3sbot', 'avatargenbot',
    'chainfuel_bot', 'polyswarmbot', 'okforexpowersignals_bot', 'etherfarm_bot', 'freematerialbot', # 40
    'novelcoronavirusbot', 'bitzoobot', 'photo2pdf_bot', 'tcryptorbot', 'simplecryptobrokerbot',
    'pswmanagerbot', 'scmpnews_bot', 'dogeninja_bot', 'zumanjibot', 'GpyNanoBot', # 50
]

s = 'on'

@bot.on_message(Filters.text, group=1)
def bot_status(cli, msg):
    if msg.text.startswith('bot ') and msg.from_user.id in admin:
        status = str(msg.text).replace('bot ', '')
        s = status
        if status == 'on':
            m = "📡 ربات روشن شد!"
        elif status == 'off':
            m = "📡 ربات روشن شد!"
        else:
            m = "📡 مشکلی در پردازش وضعیت رخ داد ، ربات به طور خودکار روشن شد!"
        msg.reply(m)

@bot.on_message(Filters.text, group=2)
def bot_on(cli, msg):
    if msg.text.startswith('start ') and msg.from_user.id in admin and not s == 'off':
        channel = str(msg.text).replace('start ', '')
        msg.reply("✅ سیستم برای افزودن تعداد {} ربات به کانال {} فعال شد.".format( len(bot_list), channel))
        c,b = 0, 0
        for i in bot_list:
            sleep(0.5)
            try:
                bot.promote_chat_member(channel, i,
                                    # can_change_info=True,
                                    # can_delete_messages=True,
                                    can_post_messages=False,
                                    # can_invite_users=True,
                                    # can_pin_messages=True,
                                    # can_edit_messages=False,
                                    # can_promote_members=True,
                                    # can_restrict_members=True
                                    )
                c += 1
            except FloodWait:
                msg.reply("""❌ محدودیت FloodWait از سمت تلگرام!
💥 ربات پس از {} ثانیه مجددا به کار خود ادامه میدهد.""".format(FloodWait.x))
                sleep(FloodWait.x)
                b += 1
            except Exception as e:
                msg.reply(e)
                b += 1
        msg.reply("""🖥 افزودن ربات به کانال به پایان رسید!
💥 تعداد ربات های اضافه شده : {}
📡 تعداد ربات هایی که اضافه نشدند : {}""".format(c, b))

bot.run()
