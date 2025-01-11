## features
- options for downloading playlist or single
- option for downloading video or audio and the formats
- server integration 

## User flow 
- user starts 
- must subscripbe to channel and the checks if subscripbed
- user sends a link 
- the bot sends back the song 


##----- user flow ----------
# start: get a hello message
# send_url: get an inline options to download the yt with the thumbnail
# choose: after choosing it will get processing text that disappers after it finished
# done 
# Global variable for subscription status


            #! this is to get the metadata to send back for now it's in hold 
            # keyboard = [
            # [InlineKeyboardButton("Download", callback_data='dwn')]
            #  ]
            # reply_markups = InlineKeyboardMarkup(keyboard)   
            # meta_data = await get_metadata(url=update.message.text)
            # await context.bot.send_photo(
            # update.effective_chat.id,
            # meta_data.get('thumbnail'),
            # caption=(
            # f"🔎{meta_data.get('title')}\n"
            # f"🔎{meta_data.get('summary')}\n"
            # ),
            # reply_markup=reply_markups
            # )

