import os

from utils.funcs import*


def test_load_data():
    assert load_data([]) is None, 'проверка на другие типы'
    assert load_data(12) is None, 'проверка на другие данные'
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

# def test_sorted_list():

