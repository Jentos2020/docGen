import pyotp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import MyStatesGroup
from keyboards import *


# двухфакторка инициализация
async def twoFaStart(msg: types.Message, state: FSMContext):
    codeExamp = '`K2UTFG25CBOPFFWWJCIZSMNCKHPBMFZA`'
    await msg.answer(text=f'Пришлите 2FA\-код, ответом получите актуальный 6\-значный код\.\nПример: {codeExamp}',
                     parse_mode='MarkdownV2', reply_markup=setTwoFAReadyKb())
    await MyStatesGroup.twoFaReady.set()

# двухфакторка обработка кода
async def twoFaReady(msg: types.Message, state: FSMContext):
    try:
        code2fa = pyotp.TOTP(msg.text)
        await msg.answer(text=f'`{code2fa.now()}`', parse_mode='MarkdownV2',)
    except:
        await msg.answer(text='\u274C Пришлите корректный код')