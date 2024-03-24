import discord
import os
from openai import OpenAI

# Discordのクライアントを作成
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# OpenAIのクライアントを初期化
openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

async def ask_openai(question):
    # OpenAIのAPIを使用して質問に答える
    chat_completion = openai_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Please perform morphological analysis on the Japanese sentences that have been input. Guess how to read anything other than hiragana in the input sentences from a series of sentence contents, and output all sentences in hiragana form."
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-4-turbo-preview",
    )
    return chat_completion.choices[0].message.content

# イベント: メッセージが送信されたとき
@client.event
async def on_message(message):
    # ボット自身のメッセージは無視
    if message.author == client.user:
        return

    # メッセージのコンソール出力
    print(f"{message.channel}: {message.author}: {message.content}")

    # OpenAIに質問を送信し、応答を取得
    response = await ask_openai(message.content)

    # OpenAIの応答をコンソールに出力
    print(f"OpenAIの応答: {response}")

# イベント: ボットが準備完了したとき
@client.event
async def on_ready():
    print(f'ログインしました: {client.user.name}')

# ここにDiscordのトークンを入力
TOKEN = 'MTIyMTAwOTIwNjg4MzI1ODM2OA.GSuJME.YtIxu3xj0hjoBBesbe6yASx_zXtrwSGYwXTFMs'

# ボットを起動
client.run(TOKEN)