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
   
    if message.content.startswith('/send'):
        send_message=message.content.split(" ")
        channel = discord.utils.get(message.guild.text_channels, name=send_message[1])
        await channel.send("[{0}]\n{1}".format(message.author.name,send_message[2]))
    
    elif message.content.startswith('/to'):
        send_message=message.content.split(" ")
        channel = discord.utils.get(message.guild.text_channels, name=send_message[1])
        await message.channel.send('ここが送信元!(送信先:{0})'.format(send_message[1]))
        await channel.send('送信先として設定(送信元:{0})'.format(message.channel.name))
        copy_message=message
        while copy_message.content != '/fin':
            copy_message=await client.wait_for("message",check=check)
            if copy_message.channel==message.channel:
                await channel.send("[{0}]{1}\n{2}".format(copy_message.channel.name,copy_message.author.display_name,copy_message.content))
        await message.channel.send('終了しました')
        await channel.send('終了しました')
        

        
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
