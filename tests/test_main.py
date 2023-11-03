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


