MESSAGE_TEXT='**Link to access the chart :** https://charts.bogged.finance/0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3'

def graph(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT , parse_mode='markdown')
