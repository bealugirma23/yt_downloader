import logging
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, MessageHandler, CommandHandler, filters
from bot.config import TOKEN
from bot.handlers import start, button, url_detail_opt, unknown

def main():
    # Basic logging setup for debugging
    # logging.basicConfig(level=logging.DEBUG)
    print(f"Loaded bot token: {TOKEN}")
    print("Bot is starting...")

    # Initialize the bot application
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))  
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, url_detail_opt)) 
    app.add_handler(MessageHandler(filters.COMMAND, unknown))
    # Run the bot
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
