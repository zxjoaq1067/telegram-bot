MESSAGE_TEXT='**Latest news**:\n\nhttps://t.me/safemoonnewsbrl'

def news(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown', disable_web_page_preview='True')
