import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token bot Telegram
TOKEN = "8707863883:AAGzZHHBvUKGfajeSZtcR5ImY6fCcgU3k8o"

# Web app URL
WEB_URL = "https://earnflowserver-production.up.railway.app/"

# Handler /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = WEB_URL

    # Optional referral code
    if context.args:
        arg = context.args[0]
        if arg.startswith("ref_"):
            ref_id = arg.replace("ref_", "")
            url = WEB_URL + "?ref=" + ref_id

    print("WEBAPP URL:", url)

    keyboard = [
        [InlineKeyboardButton("🚀 Open EarnFlow", web_app=WebAppInfo(url=url))]
    ]

    await update.message.reply_text(
        "Welcome! Start earning now 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Build bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Railway webhook setup
PORT = int(os.environ.get("PORT", 8443))
RAILWAY_URL = os.environ.get("RAILWAY_STATIC_URL")  # Isi di Env Railway

WEBHOOK_URL = f"{RAILWAY_URL}/{TOKEN}" if RAILWAY_URL else None
if WEBHOOK_URL:
    print("Webhook URL set to:", WEBHOOK_URL)
else:
    print("No RAILWAY_STATIC_URL found, using polling fallback (for testing only)")

# Jalankan bot
if WEBHOOK_URL:
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL
    )
else:
    app.run_polling()

print("Bot is running...")
