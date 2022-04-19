# THIS`IS TLEGRAM_BOT
import json
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import AndroidVacance
import IOSVacance
import todaysVacacies
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)

dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def welcomeMessages(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Web -Бағдарламалау')
    item2 = types.KeyboardButton('Android -Бағдарламалау')
    item3 = types.KeyboardButton('IOS -Бағдарламалау')
    markup.add(item1, item2, item3)
    await message.answer("Cәлем {0.first_name}\n Сенің телеграм бот асистентің!".format(message.from_user),
                         reply_markup=markup)


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    photo = open('logo.jfif','rb')
    await message.answer_photo(photo)
    await message.answer("{0.first_name}\n Сенің телеграм бот асистентің!".format(message.from_user)
                         + "\n/about - Пайдаланушы нұсқаулығы"
                         + "\n/vacancies - Күннің 10 үздік ұсынысы!")



@dp.message_handler(commands=['vacancies'])
async def vacancies(message: types.Message):
    photo = open('logo.jfif', 'rb')
    await message.answer_photo(photo)
    inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159t')
    inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160t')
    inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205t')
    back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
    await message.answer("Күннің 10 үздік ұсынысы!", reply_markup=inline_kb1)

@dp.message_handler(content_types=['text'])
async def bot_Messages(message: types.Message):
    if message.text == 'Web -Бағдарламалау':
        photo = open("Web-Developer.jpeg", 'rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Front-end Бағдарламалау', callback_data='Front-end dev!')
        inline_btn_2 = InlineKeyboardButton('Back-end Бағдарламалау', callback_data='Back-end dev!')
        inline_btn_3 = InlineKeyboardButton('Full-stack Бағдарламалау', callback_data='Full-stack dev!')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer(
            "{0.first_name}\n- сіз \'Web -Бағдарламалау\' бөліміндесіз! \nСенің телеграм бот асистентің!".format(
                message.from_user), reply_markup=inline_kb1)
    elif message.text == 'Android -Бағдарламалау':
        photo = open("android.jpeg", 'rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159')
        inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160')
        inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer(
            "{0.first_name}\n- сіз \'Android -Бағдарламалау\' бөліміндесіз \n Сенің телеграм бот асистентің!".format(
                message.from_user), reply_markup=inline_kb1)
    elif message.text == 'IOS -Бағдарламалау':
        photo = open('iOS-Developer.jpg','rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159i')
        inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160i')
        inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205i')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer(
            "{0.first_name}\n- сіз \'IOS -Бағдарламалау\' бөліміндесіз \n Сенің телеграм бот асистентің!".format(
                message.from_user), reply_markup=inline_kb1)

    elif message.text == '⬅ Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Web - Бағдарламалау')
        item2 = types.KeyboardButton('Android - Бағдарламалау')
        item3 = types.KeyboardButton('IOS - Бағдарламалау')
        markup.add(item1, item2, item3)
        await message.answer(
            "{0.first_name}\nYou tap to \'⬅ Back\' button \n your assistant telegram bot!".format(
                message.from_user), reply_markup=markup)



@dp.callback_query_handler()
async def process_callback_btn(callback_query: types.CallbackQuery):
    if callback_query.data == 'Front-end dev!':
        photo = open("img.png",'rb')
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_photo(callback_query.message.chat.id, photo)
        f = open('Front-end.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
             await bot.send_message(callback_query.message.chat.id,v['alternate_url'],parse_mode='html')
        print(callback_query.from_user.first_name)
        await bot.send_message(callback_query.from_user.id, 'Front-end Бағдарламалау бөліміндесіз!')
    elif callback_query.data == '⬅ Back':
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id,callback_query.message.message_id)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    elif callback_query.data == 'Back-end dev!':
        await bot.answer_callback_query(callback_query.id)
        f = open('Back-end.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == 'Full-stack dev!':
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        f = open('Full-stack.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id,v['alternate_url'], parse_mode='html')
    elif callback_query.data == '159':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        photo = open("android.jpeg", "rb")
        await bot.send_photo(callback_query.message.chat.id, photo)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы бойынша бос жұмыс орындары тізімі:")
        AndroidVacance.parse(int(callback_query.data))
        f = open('Android.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '205':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        photo = open("android.jpeg", "rb")
        await bot.send_photo(callback_query.message.chat.id, photo)
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы бойынша бос жұмыс орындары тізімі:")
        AndroidVacance.parse(int(callback_query.data))
        f = open('Android.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '160':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        photo = open("android.jpeg", "rb")
        await bot.send_photo(callback_query.message.chat.id, photo)
        await bot.send_message(callback_query.message.chat.id,"Алматы қаласы бойынша бос жұмыс орындары тізімі:")
        AndroidVacance.parse(int(callback_query.data))
        f = open('Android.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '159i':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        photo = open("iOS-Developer.jpg", "rb")
        await bot.send_photo(callback_query.message.chat.id, photo)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы бойынша бос жұмыс орындары тізімі:")
        IOSVacance.parse(int(callback_query.data[:-1]))
        f = open('IOS development.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    elif callback_query.data == '205i':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        photo = open("iOS-Developer.jpg", "rb")
        await bot.send_photo(callback_query.message.chat.id, photo)
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы бойынша бос жұмыс орындары тізімі:")
        IOSVacance.parse(int(callback_query.data[:-1]))
        f = open('IOS development.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '160i':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        photo = open("iOS-Developer.jpg", "rb")
        await bot.send_photo(callback_query.message.chat.id, photo)
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы бойынша бос жұмыс орындары тізімі:")
        IOSVacance.parse(int(callback_query.data[:-1]))
        f = open('IOS development.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '159t':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы бойынша бос жұмыс орындары тізімі:")
        todaysVacacies.parse(int(callback_query.data[:-1]))
        f = open('Top10.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '205t':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы бойынша бос жұмыс орындары тізімі:")
        todaysVacacies.parse(int(callback_query.data[:-1]))
        f = open('Top10.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
    elif callback_query.data == '160t':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы бойынша бос жұмыс орындары тізімі:")
        todaysVacacies.parse(int(callback_query.data[:-1]))
        f = open('Top10.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

        # inline_btn_1 = InlineKeyboardButton('Front-end dev!', callback_data='Front-end dev!') ,reply_markup=markup
        # inline_btn_2 = InlineKeyboardButton('Back-end dev!', callback_data='Back-end dev!')
        # inline_btn_3 = InlineKeyboardButton('Full-stack dev!', callback_data='Full-stack dev!')
        # back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        # inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        # await message.answer(
        #     "{0.first_name}\nYou tap to \'Web -разработка\' button \n your assistant telegram bot!".format(
        #         message.from_user), reply_markup=inline_kb1)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
