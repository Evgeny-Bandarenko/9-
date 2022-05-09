from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='тут свой токен')
dp = Dispatcher(bot)
OTHER_MSG_CHAT_ID = '-11111'
CHATS = {
    'отгрузка': {
        'chat_id': '-111111',
        'message_patterns': [
            'загрузка',
            'погрузка',
            'выгрузка',
            'отгрузка',
        ],
        'to_print': '<b>Заявка для отгрузки</b>\n\n'
    },
    'перевозка': {
        'chat_id': '-11111',
        'message_patterns': [
            'перевозка',
            'перевоз',
            'перевозить',
            'отвозить',
            'доставка',
            'доставить',
        ],
        'to_print': '<b>Заявка для перевозки</b>\n\n'
    }
}
@dp.message_handler(chat_type=[types.ChatType.GROUP, types.ChatType.PRIVATE, types.ChatType.SUPERGROUP])
async def process_lead(message):
    is_sent = False
    if message.chat.id != -1001707017327 and message.chat.id != -1001636033300:
        for chat_name, content in CHATS.items():
            chat_id = content['chat_id']
            for allowed_word in content['message_patterns']:
                if allowed_word in message.text.lower():
                    await bot.send_message(chat_id, content['to_print'] + message.text, parse_mode='html')
                    await message.reply('Заявка ушла в <b>%s:</b>\n\n' % chat_name, parse_mode='html')
                    is_sent = True
                    break
    if not is_sent:
        await bot.send_message(OTHER_MSG_CHAT_ID, '<b>Неразобранная заявка:</b>\n\n' + message.text, parse_mode='html')
        await message.reply('Заявка ушла в <b>остальное:</b>\n\n', parse_mode='html')
executor.start_polling(dp)