import requests

chat_id = "6236388211"
urlp = "https://t.me/elhyba"
url = f"https://api.telegram.org/bot7252102565:AAH3gTkB7vAwRxO8DA76X6-DKRQb7PLuQcw/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
