from pyrogram import Client, filters

bot_token = "7252102565:AAH3gTkB7vAwRxO8DA76X6-DKRQb7PLuQcw"

api_id = 24514467
api_hash = "5a8c3d38c4d89b672062c5ff015380c7"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

