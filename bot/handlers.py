
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes
from utils.checkMember import is_member_method 
from services.yt_dlp import sending_audio, get_metadata
logger = logging.getLogger(__name__)
import validators
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    try: 
        print("started.............")
        keyboard = [
            [InlineKeyboardButton("Check", callback_data="opt1")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Send hello message 
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=("Hello 👋 , Please join this Please join [this channel](https://t.me/maleda_design) to use this bot."),
            parse_mode="Markdown",
            reply_markup=reply_markup, 
        )
    except Exception as e: 
        print("This is the Error: " + str(e))

# For handling button queries for checking the subscription
async def button(update: Update,context: ContextTypes.DEFAULT_TYPE):
    global isSubscribed  # Declare the use of the global variable
    query = update.callback_query
    await query.answer()

    if query.data == "opt1":
        print(update.effective_user.id,"test")
        isMember = await is_member_method(user_id=update.effective_user.id, context=context)
        if isMember:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=("😀Horray!!!!!!!!!"))
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=("Thank You, you can now send any youtube url for download"),
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=("You have to subscribe first to send a link."),
            )
        #  after subscription it should 
async def url_detail_opt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    isSubscribed = await is_member_method(user_id=update.effective_user.id, context=context)
    if isSubscribed:
        validUrl = validators.url(update.message.text)
        if validUrl:
            to_delete =await update.message.reply_text("Processing...")
            try:
                # Download the audio
                file_path = await sending_audio(url=update.message.text)
                if file_path:
                    # Send the audio file to the user
                    with open(file_path, 'rb') as audio:
                        print(to_delete.message_id, "sos")
                        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=to_delete.message_id)
                        await context.bot.send_audio(chat_id=update.effective_chat.id, audio=audio)
                    
                    # Remove the file after sending
                    os.remove(file_path)
                else:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, couldn't download the song.")
            except Exception as e:
                await context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred. Please try again.")
                print(e, "error")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="😖 It's not a valid URL.")
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You haven't subscribed yet. Please join [this channel](https://t.me/maleda_design) to use this bot.",
            parse_mode="Markdown"
        )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Sorry, I didn't understand that command."
    )



# Check subscription status when a user sends a message
# async def url_detail_opt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
#     isSubscribed = await is_member_method(user_id=update.effective_user.id, context=context)
#     if isSubscribed:
   #      validUrl = validators.url(update.message.text)
   #      if(validUrl):
   #          await context.bot.send_message(
   #          chat_id=update.effective_chat.id,
   #          text=("Processing..."))
   #          try:
   #            song = await sending_audio(url=update.message.text)
   #            if(song):
   #               lst = os.path.join("uploads", song[0])
   #               await context.bot.send_audio(chat_id=update.effective_chat.id, audio=lst)
   #               os.__file__.remove(song) 
   #            else: 
   #               await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry can't find the song")
   #          except Exception as e:
   #             await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry some Error just happened")
   #             print(e)
   #          # print(s)
   #      else:
   #          await context.bot.send_message(chat_id=update.effective_chat.id, text=("😖it's not a valid url"))
   #  else:
   #      await context.bot.send_message(
   #          chat_id=update.effective_chat.id,
   #          text=("You haven't subscribed yet. Please join [this channel](https://t.me/maleda_design) to use this bot."),
   #      )

