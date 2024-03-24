import discord

# Discordのクライアントを作成
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# イベント: メッセージが送信されたとき
@client.event
async def on_message(message):
    # ボット自身のメッセージは無視
    if message.author == client.user:
        return

    # メッセージの内容と送信者をコンソールに出力
    print(f"{message.channel}: {message.author}: {message.content}")

# イベント: ボットが準備完了したとき
@client.event
async def on_ready():
    print(f'ログインしました: {client.user.name}')

# ここにDiscordのトークンを入力
TOKEN = 'MTIyMTAwOTIwNjg4MzI1ODM2OA.GSuJME.YtIxu3xj0hjoBBesbe6yASx_zXtrwSGYwXTFMs'

# ボットを起動
client.run(TOKEN)