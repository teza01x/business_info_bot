import asyncio
import aiohttp
import aiofiles
import time
import re
from datetime import datetime, timedelta
from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup
from telebot import types
from async_sql_scripts import *
from async_markdownv2 import *
from text_scripts import *
from config import *


bot = AsyncTeleBot(telegram_token)


@bot.message_handler(commands=['start', 'menu'])
async def start(message):
    try:
        user_id = message.from_user.id
        username = message.from_user.username

        if not await check_user_exists(user_id):
            try:
                await add_user_to_db(user_id, username)
            except Exception as error:
                print(f"Error adding user to db error:\n{error}")
        else:
            await update_username(user_id, username)

        text = await escape(dictionary['start_msg'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Оставить заявку на назначение термина", callback_data="submit_app"),
        ]
        button_list2 = [
            types.InlineKeyboardButton("Запросить звонок", callback_data="request_call"),
        ]
        button_list4 = [
            types.InlineKeyboardButton("Связаться с консультантом", callback_data="request_consult"),
        ]
        button_list5 = [
            types.InlineKeyboardButton("Информация о компании", callback_data="company_info"),
        ]
        button_list6 = [
            types.InlineKeyboardButton("Перечень услуг", callback_data="service_list"),
        ]
        button_list7 = [
            types.InlineKeyboardButton("Ответы на частые вопросы", callback_data="answer_on_often_quests"),
        ]
        button_list8 = [
            types.InlineKeyboardButton("Как оплатить услугу?", callback_data="how_to_pay_service"),
        ]
        button_list9 = [
            types.InlineKeyboardButton("Как оплатить страховку?", callback_data="how_to_pay_insurance"),
        ]
        button_list9 = [
            types.InlineKeyboardButton("Как оплатить страховку?", callback_data="how_to_pay_insurance"),
        ]
        button_list10 = [
            types.InlineKeyboardButton("Ссылки на компании", callback_data="company_links"),
        ]
        button_list11 = [
            types.InlineKeyboardButton("Ссылки на компании", callback_data="company_links"),
        ]
        button_list12 = [
            types.InlineKeyboardButton("Советы на приеме у врача", callback_data="advices"),
        ]
        button_list13 = [
            types.InlineKeyboardButton("Задать вопрос", callback_data="ask_question"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1, button_list2, button_list4, button_list5, button_list6, button_list7,
                                                   button_list8, button_list9, button_list10, button_list11, button_list12, button_list13])

        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")
        await change_menu_status(user_id, 0)

    except Exception as e:
        print(f"Error in start message: {e}")


@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    user_id = call.from_user.id
    username = call.from_user.username

    if call.data == "submit_app":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['phone_number'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")
        await change_menu_status(user_id, phone_number_status)

    elif call.data == "request_call":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['phone_number'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")
        await change_menu_status(user_id, phone_number_status)

    elif call.data == "request_consult":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['phone_number'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")
        await change_menu_status(user_id, phone_number_status)

    elif call.data == "ask_question":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['ask_quest'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")
        await change_menu_status(user_id, ask_question_status)

    elif call.data == "company_info":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['company_info'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "service_list":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['service_list'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "answer_on_often_quests":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['answer_on_often_quests'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "how_to_pay_service":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['how_to_pay_service'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "how_to_pay_insurance":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['how_to_pay_insurance'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "company_links":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['company_links'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "advices":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['advices'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Back ⬅️", callback_data="start_menu"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")

    elif call.data == "start_menu":
        await bot.answer_callback_query(call.id)

        text = await escape(dictionary['start_msg'], flag=0)

        button_list1 = [
            types.InlineKeyboardButton("Оставить заявку на назначение термина", callback_data="submit_app"),
        ]
        button_list2 = [
            types.InlineKeyboardButton("Запросить звонок", callback_data="request_call"),
        ]
        button_list4 = [
            types.InlineKeyboardButton("Связаться с консультантом", callback_data="request_consult"),
        ]
        button_list5 = [
            types.InlineKeyboardButton("Информация о компании", callback_data="company_info"),
        ]
        button_list6 = [
            types.InlineKeyboardButton("Перечень услуг", callback_data="service_list"),
        ]
        button_list7 = [
            types.InlineKeyboardButton("Ответы на частые вопросы", callback_data="answer_on_often_quests"),
        ]
        button_list8 = [
            types.InlineKeyboardButton("Как оплатить услугу?", callback_data="how_to_pay_service"),
        ]
        button_list9 = [
            types.InlineKeyboardButton("Как оплатить страховку?", callback_data="how_to_pay_insurance"),
        ]
        button_list10 = [
            types.InlineKeyboardButton("Ссылки на компании", callback_data="company_links"),
        ]
        button_list11 = [
            types.InlineKeyboardButton("Ссылки на компании", callback_data="company_links"),
        ]
        button_list12 = [
            types.InlineKeyboardButton("Советы на приеме у врача", callback_data="advices"),
        ]
        button_list13 = [
            types.InlineKeyboardButton("Задать вопрос", callback_data="ask_question"),
        ]
        reply_markup = types.InlineKeyboardMarkup([button_list1, button_list2, button_list4, button_list5, button_list6, button_list7,
                                                   button_list8, button_list9, button_list10, button_list11, button_list12, button_list13])

        await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=reply_markup, parse_mode="MarkdownV2")
        await change_menu_status(user_id, start_status)


async def is_valid_phone_number(phone):
    pattern = r"^\+?[1-9]\d{7,11}$"
    return re.match(pattern, phone) is not None

# сделать тут обработку текстовых сообщений от юзера, с проверкой статуса и приемом номера телефона (написать функцию, проверяющую ввод на правильность номера тлф)

@bot.message_handler(func=lambda message: True, content_types=['text'])
async def handle_text(message):
    chat_type = message.chat.type
    if chat_type == 'private':
        user_id = message.chat.id
        username = message.chat.username
        first_name = message.chat.first_name
        last_name = message.chat.last_name

        if last_name == None:
            last_name = ""

        user_status = await get_user_status(user_id)

        if user_status == phone_number_status:
            phone = message.text
            phone_status = await is_valid_phone_number(phone)
            if phone_status == True:
                text = await escape(dictionary["app_submitted"], flag=0)
                await bot.send_message(chat_id=message.chat.id, text=text, parse_mode="MarkdownV2")

                text = await escape(dictionary["subm_app_form"].format(username, first_name, last_name, phone), flag=0)
                await bot.send_message(chat_id=group_id_for_notifications, text=text, parse_mode="MarkdownV2")
                await change_menu_status(user_id, start_status)
            else:
                text = await escape(dictionary["incorrect_number"], flag=0)
                await bot.send_message(chat_id=message.chat.id, text=text, parse_mode="MarkdownV2")

        elif user_status == ask_question_status:
            question = message.text
            text = await escape(dictionary["quest_submitted"], flag=0)
            await bot.send_message(chat_id=message.chat.id, text=text, parse_mode="MarkdownV2")

            text = await escape(dictionary["subm_app_form_quest"].format(username, first_name, last_name, question), flag=0)
            await bot.send_message(chat_id=group_id_for_notifications, text=text, parse_mode="MarkdownV2")
            await change_menu_status(user_id, start_status)




async def main():
    try:
        bot_task = asyncio.create_task(bot.polling(non_stop=True, request_timeout=500))
        await asyncio.gather(bot_task)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()