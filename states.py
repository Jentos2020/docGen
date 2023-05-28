from aiogram.dispatcher.filters.state import StatesGroup, State


class MyStatesGroup(StatesGroup):
    main = State()
    imgStart = State()
    imgReady = State()
    twoFaStart = State()
    twoFaReady = State()