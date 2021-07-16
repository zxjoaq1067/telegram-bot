MESSAGE_TEXT='**How to buy Safemoon:** https://www.youtube.com/watch?v=J-68f5ybj-o'

def video(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
