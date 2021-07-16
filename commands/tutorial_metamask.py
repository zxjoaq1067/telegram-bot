MESSAGE_TEXT='**How to add binance smart chain network in Metamask:** https://docs.binance.org/smart-chain/wallet/metamask.html'
def metamask(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
