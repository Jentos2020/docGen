from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def setMainKb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Сгенерировать фото')
    btn2 = KeyboardButton(text='Получить 2FA код')
    kb.add(btn1, btn2)
    return kb

def setImgStartKb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Еще')
    btn2 = KeyboardButton(text='Главное меню')
    kb.add(btn1).add(btn2)
    return kb

def setImgReadyKb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Еще')
    btn2 = KeyboardButton(text='Главное меню')
    kb.add(btn1, btn2)
    return kb

def setTwoFAReadyKb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Главное меню')
    kb.add(btn1)
    return kb