@bot.event
async def on_message(msg):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',msg.content.lower())
    if not urls:
        return msg
    if urls and not msg.author.top_role.permissions.manage_messages:
        await msg.delete()
        await msg.channel.send("No puedes enviar enlaces en este servidor")

@bot.event
async def on_message_edit(bf,af):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',af.content.lower())
    if urls and not af.author.top_role.permissions.manage_messages:
        await af.delete()
        await af.channel.send("No puedes enviar enlaces en este servidor")