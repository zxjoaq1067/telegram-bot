import requests
from bs4 import BeautifulSoup

def get_holders():
  try:
    response = requests.get("https://bscscan.com/token/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3")
    soup = BeautifulSoup(response.content, 'html.parser')
    holders = soup.select("#ContentPlaceHolder1_tr_tokenHolders > div > div.col-md-8 > div > div")
    result = holders[0].text
    result = result.replace('\n', '')
  except:
    result = ''
  return result

def get_coins_available_to_buy():
  try:
    response = requests.get("https://bscscan.com/token/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3")
    soup = BeautifulSoup(response.content, 'html.parser')
    holders = soup.select("#ContentPlaceHolder1_divFilteredHolderBalance")
    result = holders[0].text
    result = result.replace('\n', '')
    result = result.replace('Balance', '')
  except:
    result = ''
  return result

def get_coins_burned():
  try:
    response = requests.get("https://bscscan.com/token/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3?a=0x000000000000000000000000000000000000dead")
    soup = BeautifulSoup(response.content, 'html.parser')
    holders = soup.select("#ContentPlaceHolder1_divFilteredHolderBalance")
    result = holders[0].text
    result = result.replace('\n', '')
    result = result.replace('Balance', '')
  except:
    result = ''
  return result

message_text = "Safemoon contract: 0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3\n\nBSC scan: https://bscscan.com/address/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3\n\n"
message_text += "Safemoon holders: {}".format(get_holders())
message_text += "\nCoins available to buy: {}".format(get_coins_available_to_buy())
message_text += "\nCoins burned: {}".format(get_coins_burned())

def contract(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message_text, parse_mode='markdown', disable_web_page_preview='True')
