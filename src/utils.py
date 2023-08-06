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