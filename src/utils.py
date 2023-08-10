from datetime import date
import json


def get_operations_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def sort_operations_by_date(operations):
    """фильтрует массив от пустых операций и сортирует по убыванию даты операции"""
    sorted_operations = sorted(operations,
                               key=lambda operations: operations['date'],
                               reverse=True)
    return sorted_operations[:5]


def get_executed_operations(operations):
    """принимает список словарей,
    возвращает массив, содержащий только исполненные операции
    в заданном количестве
    """
    executed_operations = []
    for operation in operations:
        if not operation:
            continue
        if operation["state"] == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def change_operation_date(operations):
    """принимает список словарей и возвращает его,
    с заданным форматом ключа 'дата'
    """
    for operation in operations:
        thedate = date.fromisoformat(operation['date'][:10])
        operation['date'] = f'{thedate.day}.{thedate.month}.{thedate.year}'
    return operations


def mask_requisites(requisite):
    list_req = requisite.split(' ')
    if list_req[0] == 'Счет':
        list_req[-1] = f'**{list_req[-1][-4:]}'
    else:
        list_req[-1] = f'{list_req[-1][:4]} {list_req[-1][4:6]}** **** {list_req[-1][-4:]}'
    return ' '.join(list_req)


def output_operations_history(operation):
    """Выводит историю операций в заданном формате"""
    first_line = f'{operation["date"]} {operation["description"]}'
    third_line = (f'{operation["operationAmount"]["amount"]} '
                 f'{operation["operationAmount"]["currency"]["name"]}')
    if operation["description"] == "Открытие вклада":
        second_line = f'-> {operation["to"]}'
    else:
        second_line = f'{operation["from"]} -> {operation["to"]}'
    operations_history = f'{first_line}\n{second_line}\n{third_line}\n'
    return operations_history

