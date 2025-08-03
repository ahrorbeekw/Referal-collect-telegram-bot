import asyncio
from aiogram import Bot, Dispatcher, types , F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery
from aiogram.utils.deep_linking import create_start_link

import asyncio
import logging
import sys
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
API_TOKEN = '7417051013:AAET_1DjQ8BHyh3BOSOwD1y38va0HJsAn5E'


dp = Dispatcher()
bot = Bot(token=API_TOKEN)
router = Router()  


users_referrals = {}

async def create_invite_link(user_id):
    link = await create_start_link(bot, user_id)
    return link


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    if ' ' in message.text:
        args = message.text.split(' ')[1]  
    else:
        args = None  


    if args:
        inviter_id = int(args)
        if inviter_id != user_id:  
            users_referrals[inviter_id] = users_referrals.get(inviter_id, 0) + 1


    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Do'st taklif qilish havolasi olish", callback_data="invite")],
        [InlineKeyboardButton(text="Taklif qilingan do'stlar soni", callback_data="ref_count")]
    ])

    await message.answer("Do'stlaringizni botga taklif qiling!", reply_markup=keyboard)


@router.callback_query(F.data.in_({"invite", "ref_count"}))
async def process_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    
    if callback_query.data == "invite":
        
        invite_link = await create_invite_link(user_id)
        await callback_query.message.answer(f"Do'st taklif qilish havolangiz: {invite_link}")
    
    elif callback_query.data == "ref_count":
        
        count = users_referrals.get(user_id, 0)
        await callback_query.message.answer(f"Siz {count} do'st taklif qildingiz!")

    await callback_query.answer()  


dp.include_router(router)

async def main() -> None:
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
