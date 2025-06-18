
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)

logging.basicConfig(level=logging.INFO)

ASK_NAME, ASK_CASE, ASK_DATE, ASK_TIME, UPLOAD_DOC = range(5)

ADMIN_CHAT_ID = "975017003"
BOT_TOKEN = "8081249119:AAGObpi9P-fMfXmcB_1HtvBTGDLXSPtEJNw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Assalomu alaykum! Men yuridik xizmatlar uchun yordamchi botman.\n"
        "Quyidagi menyudan birini tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            [["📅 Uchrashuv band qilish", "📤 Hujjat yuborish"], ["❓ Savollar"]],
            resize_keyboard=True,
        )
    )

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📅 Uchrashuv band qilish":
        await update.message.reply_text("Ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())
        return ASK_NAME
    elif text == "📤 Hujjat yuborish":
        await update.message.reply_text("PDF yoki rasmni yuboring.")
        return UPLOAD_DOC
    elif text == "❓ Savollar":
        await update.message.reply_text(
            "📌 Savollar:\n"
            "- Narxlarimiz shaxsiy holatlarga bog‘liq.\n"
            "- Immigratsiya, nikohdan ajrashish, kontraktlar bo‘yicha maslahatlar beramiz.\n"
            "- Ish kunlari: Dushanba–Juma, soat 9:00–18:00."
        )
    return ConversationHandler.END

async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Qisqacha holatingizni yozing (masalan: ajrashish, qarzdorlik va h.k.)")
    return ASK_CASE

async def ask_case(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["case"] = update.message.text
    await update.message.reply_text("Uchrashuv kunini kiriting (masalan: 2025-06-20)")
    return ASK_DATE

async def ask_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["date"] = update.message.text
    await update.message.reply_text("Uchrashuv vaqtini kiriting (masalan: 14:30)")
    return ASK_TIME

async def ask_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["time"] = update.message.text

    message = (
        f"📅 *Yangi uchrashuv band qilindi:*\n"
        f"👤 Ismi: {context.user_data['name']}\n"
        f"📂 Holati: {context.user_data['case']}\n"
        f"🗓 Sana: {context.user_data['date']} soat {context.user_data['time']}"
    )

    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message, parse_mode="Markdown")
    await update.message.reply_text("✅ Uchrashuv so‘rovi yuborildi. Tez orada siz bilan bog‘lanamiz.")
    return ConversationHandler.END

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document or update.message.photo[-1]
    file = await doc.get_file()
    await context.bot.send_document(chat_id=ADMIN_CHAT_ID, document=file.file_id, caption="📤 Yangi hujjat yuborildi.")
    await update.message.reply_text("✅ Hujjat muvaffaqiyatli qabul qilindi.")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Jarayon bekor qilindi.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT, ask_name)],
            ASK_CASE: [MessageHandler(filters.TEXT, ask_case)],
            ASK_DATE: [MessageHandler(filters.TEXT, ask_date)],
            ASK_TIME: [MessageHandler(filters.TEXT, ask_time)],
            UPLOAD_DOC: [MessageHandler(filters.Document.ALL | filters.PHOTO, handle_document)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)

    print("✅ Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
