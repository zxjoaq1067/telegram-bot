import requests
from datetime import datetime


def get_api_data(url):

    try:
        response = requests.get(url, timeout=5)
        result = response.json()
        if 'message' in result:
            result = {}
    except requests.exceptions.RequestException:
        result = {}
    except:
        result = {}
    return result

def price(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode='markdown')


usd_brl_api = get_api_data('https://api.binance.com/api/v3/ticker/price?symbol=USDTBRL')
if 'price' not in usd_brl_api:
    message_text = 'binance API down. Try again in a few minutes.'
else:
    usd_brl = usd_brl_api['price']

    pancakeswap = get_api_data('https://api.pancakeswap.info/api/v2/tokens/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3')
    if pancakeswap:
        safemoon = pancakeswap.get('data')
        timestamp = pancakeswap.get('updated_at')
        humantime = datetime.fromtimestamp(int(timestamp/1000))
        safemoon_usd = pancakeswap.get('data', {}).get('price')
        safemoon_bnb = pancakeswap.get('data', {}).get('price_BNB')
    
        if usd_brl:
            value_brl = float(usd_brl)
            value_usd = float(safemoon_usd)
            safemoon_brl = round(value_brl * value_usd, 20)
    
            message_text = '**Safemoon price USD:** ${}\n'.format(safemoon_usd)
            message_text += '**Safemoon price BNB:** ${}\n'.format(safemoon_bnb)
            message_text += '**Safemoon price BRL:** R${}\n\n'.format(safemoon_brl)
            message_text += 'Update at: {}'.format(humantime)
        else:
            message_text = 'api.pancakeswap.info down. Try again in a few minutes.'
    else:
        usd = get_api_data('https://bsc.api.0x.org/swap/v1/price?sellToken=0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3&buyToken=BUSD&sellAmount=1')
        bnb = get_api_data('https://bsc.api.0x.org/swap/v1/price?sellToken=0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3&buyToken=BNB&sellAmount=1')
        if usd and bnb:
            safemoon_usd = usd.get('price')
            safemoon_bnb = bnb.get('price')
            if usd_brl:
                value_brl = float(usd_brl)
                value_usd = float(safemoon_usd)
                safemoon_brl = round(value_brl * value_usd, 20)
                message_text = '**Safemoon price USD:** ${}\n'.format(safemoon_usd)
                message_text += '**Safemoon price BNB:** ${}\n'.format(safemoon_bnb)
                message_text += '**Safemoon price BRL:** R${}'.format(safemoon_brl)
            else:
                message_text = 'bsc.api.0x.org down. Try again in a few minutes.'
        else:
            message_text = 'Pancakeswap.info and bsc.api.0x.org API down. Try again in a few minutes.'
