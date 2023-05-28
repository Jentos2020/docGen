from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from hand_funcs.image_funcs import *
from hand_funcs.twofa_funcs import *
from states import MyStatesGroup
from keyboards import *


async def main(msg: types.Message, state: FSMContext):
    await msg.answer(text='Главное меню', reply_markup=setMainKb())
    await state.reset_state()


def registerUserHandlers(dp: Dispatcher):
    dp.register_message_handler(main, commands=['start'])
    dp.register_message_handler(main, Text(equals='Главное меню'), state=MyStatesGroup.all_states)
    dp.register_message_handler(imgStart, Text(equals='Сгенерировать фото'))
    dp.register_message_handler(imgReady, state=MyStatesGroup.imgReady)
    dp.register_message_handler(imgReady, Text(equals='Еще'), state=MyStatesGroup.imgReady)
    dp.register_message_handler(twoFaStart, Text(equals='Получить 2FA код'))
    dp.register_message_handler(twoFaReady, state=MyStatesGroup.twoFaReady)