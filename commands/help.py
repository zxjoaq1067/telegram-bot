MESSAGE_TEXT='Commands available to Safemoon:\n/site\tSafemoon official website\n/video\tDisplay tutorials in video\n/contract\tDisplay Safemoon contract\n/price\tDisplay current Safemoon price\n/metamask\tTutorial for metamask\n/trust\tTutorial for trust wallet\n/graph\tDisplay the Safemoon graph\n/news\tDisplay the latest news\n/discord\tOfficial Safemoon Discord/\n/store\tOfficial Safemoon Store \n/twitter\tOfficial Twitter\n/instagram\tOfficial Instagram\n/tokenomics\tDisplay Tokenomics\n/help\tDisplay this help message'

def safemoon_help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=MESSAGE_TEXT)
