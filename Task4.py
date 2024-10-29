# Завдання №4. За допомогою python та бібліотеки telethon виконати наступні дії з Telegram:
# a. отримати перелік користувачів будь-якого чата/пабліку
# b. відправити повідомлення якомусь контакту напряму або опублікувати повідомлення в чат/паблік

from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsSearch

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

client = TelegramClient('session_name', api_id, api_hash)

async def main():

    await client.start(phone_number)

    dialogs = await client.get_dialogs(limit=10)

    print("Оберіть чат або публічний канал:")
    for i, dialog in enumerate(dialogs):
        print(f"{i}. {dialog.title}")

    chat_index = int(input("Введіть номер чату: "))
    target_chat = dialogs[chat_index]

    participants = await client.get_participants(target_chat, filter=ChannelParticipantsSearch(''), limit=100)
    print("Список користувачів:")
    for participant in participants:
        if hasattr(participant, 'username'):
            print(f"Username: {participant.username}, Full Name: {participant.first_name} {participant.last_name}")

    message = input("Введіть повідомлення для відправлення: ")
    await client.send_message(target_chat, message)
    print("Повідомлення успішно відправлено!")

with client:
    client.loop.run_until_complete(main())