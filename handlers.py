from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import *


class MyStatesGroup(StatesGroup):
    main = State()
    imgStart = State()
    imgReady = State()
    twoFaStart = State()
    twoFaReady = State()


async def main(msg: types.Message, state: FSMContext):
    await msg.answer(text='Главное меню', reply_markup=setMainKb())
    await state.reset_state()

async def imgStart(msg: types.Message, state: FSMContext):
    await msg.answer(text='Пришлите данные в формате: Имя Фамилия дд-мм-гггг пол(м/ж) страна(UA/KZ/USA) делать лиметаданные(+/-)\nПример: Иван Иванов 24-08-1998 М UA +',
                     reply_markup=setImgStartKb()
                     )
    await MyStatesGroup.imgReady.set()
    
async def imgReady(msg: types.Message, state: FSMContext):
    await state.update_data(imgData=msg.text)
    imgData = await state.get_data()
    a = imgData['imgData'].split()
    print(a)
    await msg.answer(text='Изображение готово', reply_markup=setImgReadyKb())
    await MyStatesGroup.imgReady.set()

def registerUserHandlers(dp: Dispatcher):
    dp.register_message_handler(main, commands=['start'])
    dp.register_message_handler(main, Text(equals='Главное меню'), state=MyStatesGroup.all_states)
    dp.register_message_handler(imgStart, Text(equals='Сгенерировать фото'))
    dp.register_message_handler(imgReady, state=MyStatesGroup.imgReady)