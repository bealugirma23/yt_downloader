from telegram import ChatMember, ChatMemberUpdated

async def is_member_method( user_id,  context) -> bool:
        try:
            channel_id = "@maleda_design"
            print(channel_id, user_id)
            check = await context.bot.get_chat_member(channel_id, user_id)
            print(check.status)
            if check.status in ["member", "administrator", "creator"]:
                return True
            return False
        except Exception as e:
            print(e)
            return False
        
