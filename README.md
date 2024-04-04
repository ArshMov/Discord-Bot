# Discord-Bot
ساخت ربات دیسکورد کار نشدنی نیست ، فقط باید روششو یاد بگیرید <br><br>

برای ساخت ربات دیسکورد باید اول کتابخونه اون رو نصب کنید: <br>
```
pip install discord
```
بعد باید برای استفاده اون رو وارد پروژه بکنید:
```
import discord
```
اما برای استفاده از اسلش کامند ها باید یک کتابخونه از داخل همین کتابخونه هم وارد کنید:
```
from discord.ext import commands
```
بعد باید بیاید یک اینستنس(نمونه) از اون کتابخونه بسازید و بهش بگید که چه دسترسی هایی داره:
```
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True
```
حالا باید بیاید و یک نمونه از خود ربات بسازید و این نمونه بالا رو بهش بدید:
```
bot = commands.Bot(command_prefix="!", intents=intents)
```
خب حالا باید یک ایونت ایجاد کنیم که وقتی کد رو اجرا میکنیم هر وقت ربات کامل اجرا شد یه پیامی بده که ما متوجه بشیم:
```
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(len(synced))
    except Exception as e:
        print(e)
```
توی این کد ما اومدیم و یوزرنیم ربات رو چاپ کردیم. حالا شما میتونید هر کار دیگه ای انجام بدید.<br>
پایین چاپ کردن یوزرنیم اومدیم و تعداد اسلش کامند هارو چاپ کردیم که برای اینکه اسلش کامند ها کار بکنن ضروریه <br><br>

خب ، حالا باید یک ایونت هم ایجاد کنیم که وقتی کاربر پیام داد ربات بیاد جواب بده:
```
@bot.event
async def on_message(message):
    if message.content == "سلام":
        await message.reply("سلام من ربات هستم")
```
اینجا میاد میگه که اگه کاربر پیام `سلام` رو فرستاده بود بیاد و بهش بگه `سلام من ربات هستم`<br><br>

حالا میخوایم یک اسلش کامند ایجاد کنیم. اما اول ببینیم اسلش کامند چیه؟<br>
خب اسلش کامند ها مثل `/help` کامند هایی هستن که کاربر وقتی اونها رو میزنه ربات یک کاری رو انجام میده. اما بخش مهمش اینجاست که پیام اون کاربر تو چت ارسال نمیشه و میشه یه حالتی کرد که فقط کاربر مورد نظر اون پیام رو ببینه<br>
حالا یه مثال:
```
@bot.tree.command(name="help", description="کامند help")
async def help(ctx: discord.Interaction):
    await ctx.response.send_message("یک کامند ساده!" ,ephemeral=True)
```
نتیجه:<br>
<img src="https://s8.uupload.ir/files/bot_wbs.png" width="1000" height="600" />
<br><br>
خب حالا تا اینجا اومدیم و ربات رو نوشتیم اما باید به ربات بگیم که ربات رو اجرا کنه:
```
bot.run("TOKEN")
```
به جای توکن هم توکن ربات خودتونو قرار میدید 
<br><br><br>
داکیومنت کتابخونه دیسکورد:
```
https://discordpy.readthedocs.io/en/stable
```
