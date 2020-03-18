import discord
import module1

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('ping'):
        await message.channel.send('Pong!')
        return
    if message.content.lower().startswith('pong'):
        await message.channel.send('Ping!')
        return
    if message.content.lower() == 'rip':
        await message.channel.send('Press F to pay respects')
        return
    if message.content.lower().startswith('oof'):
        await message.channel.send(module1.oof())
        return

client.run('NTQ3NTA5Mzg3NzQ1NTU4NTI4.XnJypQ.WDS2yGFSR9f1-7AE-dJNiVdyqfU')