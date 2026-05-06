# bot.py - Telegram bot for EarnFlow (Railway-ready webhook version)

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables from .env (optional but recommended)
load_dotenv()

# Telegram Bot Token - bisa juga taruh di Railway Environment Variables
TOKEN = os.getenv("TELEGRAM_TOKEN", "8707863883:AAGzZHHBvUKGfajeSZtcR5ImY6fCcgU3k8o")

# Web App URL
WEB_URL = "https://merry-crisp-5b383c.netlify.app/?v=ref_fix2"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = WEB_URL

    # optional referral parameter
    if context.args:
        arg = context.args[0]
        if arg.startswith("ref_"):
            ref_id = arg.replace("ref_", "")
            url = WEB_URL + "&ref=" + ref_id

    print("WEBAPP URL:", url)  # optional log for debugging

    keyboard = [
        [InlineKeyboardButton("🚀 Open EarnFlow", web_app=WebAppInfo(url=url))]
    ]

    await update.message.reply_text(
        "Welcome! Start earning now 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Initialize the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add /start handler
app.add_handler(CommandHandler("start", start))

# Railway webhook setup
PORT = int(os.environ.get("PORT", 8443))  # Railway provides PORT automatically
RAILWAY_URL = os.environ.get("https://earnflowserver-production.up.railway.app/")  # Optional: custom domain / Railway project URL

WEBHOOK_URL = f"{RAILWAY_URL}/{TOKEN}" if RAILWAY_URL else None
if WEBHOOK_URL:
    print("Webhook URL set to:", WEBHOOK_URL)
else:
    print("No https://earnflowserver-production.up.railway.app/ found, using localhost fallback (testing only)")

# Start the bot with webhook
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)

print("Bot is running (webhook mode)...")
