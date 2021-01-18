# インストールした discord.py を読み込む
import discord
import os


# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']
# 接続に必要なオブジェクトを生成
client = discord.Client()
CID = 725325208537530370
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #条件に当てはまるメッセージかチェックし正しい場合は返す
    def check(msg):
        return msg.author == message.author
    
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/here to':
        await message.channel.send('ここが送信元!送信先を教えてね！')
        wait_message=await client.wait_for("message",check=check)
        CID=int(wait_message.content)
        channel = client.get_channel(CID)
        await channel.send('送信先として設定')
        copy_message=wait_message
        while copy_message.content != '/fin':
            copy_message=await client.wait_for("message",check=check)
            if copy_message.channel==message.channel:
                await channel.send("[**{1}**]__***{2}***__\n> {3}".format(copy_message.channel.name,copy_message.author.name,copy_message.content))
        await message.channel.send('終了しました')
        await channel.send('終了しました')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
