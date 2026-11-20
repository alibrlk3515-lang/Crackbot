
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🤖 Bot Hakkında", "📋 Yardım"],
        ["👋 Selam"]
    ]
    menu = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🔥 Crackbot'a hoş geldin!",
        reply_markup=menu
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🤖 Bot Hakkında":
        await update.message.reply_text("Ben Crackbot! 🚀")
    elif text == "📋 Yardım":
        await update.message.reply_text("/start - Başlat\n/help - Yardım")
    elif text == "👋 Selam":
        await update.message.reply_text("Selam kanka! 😎")
    else:
        await update.message.reply_text("Mesajını aldım! 🔥")

def main():
    token = os.environ["BOT_TOKEN"]
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    app.run_polling()

if __name__ == "__main__":
    main()
