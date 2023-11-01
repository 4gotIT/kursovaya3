import funcs, os

def main():
    """Программа загружает из json файла данные, фильтрует по успешным операциям,
    затем сортируется по дате, выводится последние 5 операций
    Затем данные счетов маскируются"""
    # Путь к файлу
    path = os.path.abspath('../operations.json')
    # Загружаем данные
    my_data = funcs.load_data(path)
    # последние 5 операций, отсортированные по дате и отформатирован формат даты
    last_operations = funcs.sort_date(funcs.sorted_list(my_data))
    formated_date_operations = funcs.convert_sort_date(last_operations)

    for operation in formated_date_operations:
        print(f'{operation["date"]} {operation["description"]}')
        print(f'{funcs.mask_numbers(operation)}')
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]['name']
        print(f'{amount} {currency}\n')


if __name__ == '__main__':
    main()