from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8707863883:AAGzZHHBvUKGfajeSZtcR5ImY6fCcgU3k8o"

WEB_URL = "https://merry-crisp-5b383c.netlify.app/?v=ref_fix2"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = WEB_URL

    if context.args:
        arg = context.args[0]

        if arg.startswith("ref_"):
            ref_id = arg.replace("ref_", "")
            url = WEB_URL + "&ref=" + ref_id

    print("WEBAPP URL:", url)

    keyboard = [
        [InlineKeyboardButton("🚀 Open EarnFlow", web_app=WebAppInfo(url=url))]
    ]

    await update.message.reply_text(
        "Welcome! Start earning now 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()
