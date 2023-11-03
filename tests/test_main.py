import os

from utils.funcs import*


def test_load_data():
    assert load_data([]) is None, 'проверка на другие типы данных'
    assert load_data(12) is None, 'проверка на другие типы данных'
    assert load_data('') is None, 'проверка на неверный путь'
    assert load_data() is None, "проверка на пустой аргумент"
    assert load_data('../operations.json')[0] == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  } , 'проверяем верно ли считывает данные из файла'

def test_sorted_list():
    test_data_1 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    test_data_2 = {
        "id": 441945886,
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    assert sorted_list() == [], 'проверка на пустой аргумент'
    assert sorted_list(2) == [], 'при других типах, возвращает пустой список'
    assert sorted_list(load_data('../operations.json')[0]) == [test_data_1], 'проверка с ключом'
    assert sorted_list(test_data_2) == [], 'проверка без ключа, возвращает пустой список'
    assert len(sorted_list(load_data('../operations.json'))) == 85, 'количество элементов с ключом == 85'

def test_sort_date():
    assert sort_date() == [], 'при пустом аргументе получаем пустой список'
    assert len(sort_date(sorted_list(load_data('../operations.json')))) == 5, 'возвращает 5 элементов'
    assert sort_date(sorted_list(load_data('../operations.json')[:3])) == [
        {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}]

def test_convert_sort_date():
    assert convert_sort_date() is None
    assert convert_sort_date(2) is None
    assert convert_sort_date([]) == []

def test_mask_numbers():
    test_data_1 = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    assert mask_numbers(test_data_1) == 'Maestro 1596 83** **** 5199 -> **9589'


