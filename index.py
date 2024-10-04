# وارد کردن ماژول دیسکورد و ماژول های اولیه
import discord
from discord.ext import commands

# ساخت یک اینستنس از دیسکورد و دادن دسترسی ها
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

# اینجا باید یک اینستنس از ربات بسازیم ولی این command_prefix زیاد به درد نمیخوره چون اسلش کامند ها هستن
bot = commands.Bot(intents=intents, command_prefix="!")

# یک ایونت on_ready ایجاد میکنیم که هر وقت ربات کامل اجرا شد صدا زده میشه
@bot.event
async def on_ready():
  # اینجا هر کاری میتونین بکنین ولی برای مثال اسم رباتی که باهاش کار میکنیم رو چاپ میکنیم
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(len(synced))
    except Exception as e:
        print(e)

# یک ایونت برای پیام های ارسال شده در گروه میسازیم که هر پیامی توی هر چنلی ارسال بشه این فانکشن صدا زده میشه
@bot.event
async def on_message(message):
    # اینجا میگیم که اگه متن پیام سلام بود ربات جواب بده سلام
    if message.content == "سلام":
        await message.reply("سلام!")

# اینجا یک اسلش کامند میسازیم که وقتی کاربر / رو میزنه یک منو طور باز میشه و اونجا کامند مارو میبینه
@bot.tree.command(name="help", description="کامند help")
async def help(ctx: discord.Interaction):
    await ctx.response.send_message("یک کامند ساده!" ,ephemeral=True)

# و در اخر توکن رباتمونو میزاریم
bot.run("TOKEN")
