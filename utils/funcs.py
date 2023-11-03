import json, os


def load_data(path=None):
    """ Функция загружает json данные и возвращает их, иначе возвращает None"""
    if isinstance(path, str):
        if os.path.isfile(path):
            with open(path, encoding='utf-8') as file:
                data = json.load(file)
                return data

def sorted_list(data=None):
    """Функция принимает список, возвращает список со
    значением state = EXECUTED"""
    sort_executed = []
    if isinstance(data, list):
        for elem in data:
            if isinstance(elem, dict):
                if elem.get('state') == 'EXECUTED':
                   sort_executed.append(elem)
    elif isinstance(data, dict):
        if data.get('state') == 'EXECUTED':
            sort_executed.append(data)
    return sort_executed


def sort_date(data=None):
    """Функция возвращает отсортированный список по убыванию
    и возвращает 5 элементов, иначе пустой список"""
    if isinstance(data, list):
        if len(data) >= 5:
            data.sort(reverse=True, key=lambda x:x['date'])
            return data[:5]
        else:
            data.sort(reverse=True, key=lambda x:x['date'])
            return data[:len(data)]
    return []

def convert_sort_date(data=None):
    """Функция конвертирует формат даты"""
    if isinstance(data, list):
        if data:
            for elem in data:
                date = elem['date'].split('T')[0]
                corect_date = date.split('-')
                if len(corect_date) == 3:
                    elem['date'] = f'{corect_date[2]}.{corect_date[1]}.{corect_date[0]}'
        else:
            return []

def mask_numbers(data: dict):
    """Функция маскирует данные счета"""
    if isinstance(data, dict):
        if data.get('to'):
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

