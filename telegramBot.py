import requests

def sendMessageByTokenAndChatId(token, chatId, message):
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatId + '&parse_mode=Markdown&text=' + message
    response = requests.get(url)
    return response.json()
