from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7846580178:AAFKS88on7VyBRvU5TUmPOuEpKMk3SOhkw4"

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hi" in text or "hello" in text:
        reply = "👋 Hello!\nWelcome to DiwaPay 💰"
    elif "register" in text:
        reply = "📝 Register here:\nhttps://mobile.diwapay.com/#/pages/auth/register?invite=SlfmRQ"
    elif "login" in text:
        reply = "🔐 Login here:\nhttps://mobile.diwapay.com"
    else:
        reply = "🤖 DiwaPay Assistant\nType: register / login"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
app.run_polling()
