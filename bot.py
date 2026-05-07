import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ========================
# CONFIG - GANTI TOKEN & WEB_URL SAJA
# ========================
TOKEN = "8707863883:AAGePtyGNttlo3EfLT1GXGKlBqFY9TBQ5G0"
WEB_URL = "https://resilient-cascaron-1b9f14.netlify.app/"
PORT = int(os.environ.get("PORT", 8443))
RAILWAY_URL = os.environ.get("RAILWAY_STATIC_URL", "https://earnflowbot-production.up.railway.app")

# ========================
# START COMMAND
# ========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = WEB_URL
    if context.args:
        arg = context.args[0]
        if arg.startswith("ref_"):
            ref_id = arg.replace("ref_", "")
            url = WEB_URL + "?ref=" + ref_id

    keyboard = [
        [InlineKeyboardButton("🚀 Open EarnFlow", web_app=WebAppInfo(url=url))]
    ]
    await update.message.reply_text(
        "Welcome! Start earning now 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ========================
# INIT BOT
# ========================
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# ========================
# WEBHOOK SETUP
# ========================
WEBHOOK_URL = f"{RAILWAY_URL}/{TOKEN}"
print("Webhook URL:", WEBHOOK_URL)

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)
print("Bot running 24/7 on Railway...")
