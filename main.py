import asyncio
from telethon import TelegramClient, events


api_id = 'token'
api_hash = 'hash'

client = TelegramClient('session_name', api_id, api_hash)

keywords = ["barber", "парихмахерская", "постричь", "барбершоп", "барбера","Постричь","Барбер","Парихмахерская","барбер","бороду","Бороду"]


async def message_monitor():
    await client.start()
    groups = await client.get_dialogs()
    for group in groups:
        if group.is_group:
            @client.on(events.NewMessage(chats=group.id))
            async def message_handler(event):
                for keyword in keywords:
                    if keyword in event.message.message:
                        print(event.message.message, 'from', group.name)
                        await client.send_message('name', event.message.message + ' from ' + group.name)
    client.add_event_handler(message_handler)
    await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(message_monitor())
