import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from docgen.creation.new_image import docMaking
from docgen.validate import validate
from states import MyStatesGroup
from keyboards import *

# докген начало
async def imgStart(msg: types.Message, state: FSMContext):
    example = '`Иван Иванов 24-08-1998 М UA +`'
    await msg.answer(text=f'Пришлите данные в формате: Имя Фамилия дд\-мм\-гггг пол\(м/ж\) страна\(UA/KZ/USA\) делать ли метаданные\(\+/\-\)\nПример: {example}',
                    parse_mode='MarkdownV2', reply_markup=setImgStartKb()
                     )
    await MyStatesGroup.imgReady.set()

# докген генерация и выдача
async def imgReady(msg: types.Message, state: FSMContext):
    if not await state.get_data():
        await state.update_data(imgData=msg.text)
    imgData = await state.get_data()
    validatedData = validate(imgData['imgData'].split())
    if validatedData:
        waiting = await msg.answer(text='\u231B_Изображение генерируется\.\.\._', parse_mode='MarkdownV2', reply_markup=setImgReadyKb())
        doc = docMaking(validatedData)
        photo = types.InputFile(doc)
        await msg.answer_document(photo)
        await waiting.delete()
        await msg.answer(text='\u2705Готово!\nДля изображения с этими же данными, нажмите кнопку «Еще», или пришлите другие данные.',
                         reply_markup=setImgReadyKb())
        os.remove(doc)
        await MyStatesGroup.imgReady.set()  
    else:
        await state.reset_state()
        await MyStatesGroup.imgReady.set()  
        important = ('*соблюдайте пробелы и формат данных*')
        example = '`Иван Иванов 24-08-1998 М UA +`'
        await msg.answer(text=f'\u274C Данные введены некорректно, {important} как в примере:\n{example}',
                         parse_mode='MarkdownV2', reply_markup=setImgReadyKb())