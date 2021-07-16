MESSAGE_TEXT='**How to add binance smart chain network in Trust Wallet:** https://academy.binance.com/pt/articles/connecting-trust-wallet-to-binance-smart-chain-bsc'

def trust(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT, parse_mode='markdown')
