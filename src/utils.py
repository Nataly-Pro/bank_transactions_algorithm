def sort_operations_by_date(operations):
    """фильтрует массив от пустых операций и сортирует по убыванию даты операции"""
    correct_operations = []
    for operation in operations:
        if operation:
            correct_operations.append(operation)
    sorted_operations = sorted(correct_operations,
                               key=lambda correct_operations: correct_operations['date'],
                               reverse=True)
    return sorted_operations


def get_some_executed_operations(operations, quantity=5):
    """принимает список словарей,
    возвращает массив, содержащий только исполненные операции
    в заданном количестве
    """
    executed_operations = []
    for operation in operations:
        if operation["state"] == "EXECUTED":
            executed_operations.append(operation)
        if len(executed_operations) == quantity:
            break
    return executed_operations
