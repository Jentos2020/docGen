def validate(data):
    dataDict = {}
    elements = len(data)
    if 5 <= elements <= 6:
        dataDict['name'] = data[0]
        dataDict['surname'] = data[1]
        if birthdayValidate(data[2]):
            dataDict['birthday'] = data[2]
        else:
            return False
        if len(data[3]) == 1:
            dataDict['sex'] = data[3]
        else:
            return False
        if (1 < len(data[4]) < 4):
            dataDict['country'] = data[4]
        else:
            return False
        if elements == 6:
            dataDict['metadata'] = True if data[5] == '+' else False
        else:
            dataDict['metadata'] = False
    return dataDict


def birthdayValidate(date):
    for i in date:
        if not (i.isdigit() or i == '-'):
            return False
    return True