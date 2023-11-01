import json, os


def load_data(path):
    """ Функция загружает json данные и возвращает их,
    если пути нет, возвращает None"""
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as file:
            data = json.load(file)
            return data
    else:
        return None

def sorted_list(data):
    """Функция принимает список, возвращает список со
    значением state = EXECUTED"""
    sort_executed = []
    for elem in data:
        if elem.get('state') == 'EXECUTED':
           sort_executed.append(elem)
    return sort_executed

def sort_date(data):
    """Функция возвращает отсортированный список по убыванию
    и возвращает 5 элементов"""
    data.sort(reverse=True, key=lambda x:x['date'])
    return data[:5]

def convert_sort_date(data):
    """Функция конвертирует формат даты"""
    for elem in data:
        date = elem['date'].split('T')[0]
        corect_date = date.split('-')
        elem['date'] = f'{corect_date[2]}.{corect_date[1]}.{corect_date[0]}'
    return data

def mask_numbers(data: dict):
    """Функция маскирует данные счета"""
    to_account = data['to'].split()
    if data.get('from'):
        from_account = data['from'].split()
        if len(from_account) == 3:
            name_account = f'{from_account[0]} {from_account[1]}'
            mask_numbers = f'{from_account[2][0:4]} {from_account[2][4:6]}** **** {from_account[2][-4:]}'
            return f"{name_account} {mask_numbers} -> **{to_account[1][-4:]}"
        else:
            name_account = f'{from_account[0]}'
            mask_numbers = f'{from_account[1][0:4]} {from_account[1][4:6]}** **** {from_account[1][-4:]}'
            return  f"{name_account} {mask_numbers} -> **{to_account[1][-4:]}"
    return f'{to_account[0]} **{to_account[1][-4:]}'

