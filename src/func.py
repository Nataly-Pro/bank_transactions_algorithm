from utils import *


def get_operations_history(json_file):
    operations = get_operations_from_file(json_file)
    sorted_operations = sort_operations_by_date(operations)
    executed_operations = get_some_executed_operations(sorted_operations)
    formatted_date_operations = change_operation_date(executed_operations)

# перебор операций в цикле для маскировки платежных реквизитов
    for operation in formatted_date_operations:
        if operation["description"] != "Открытие вклада":
            operation["from"] = mask_requisites(operation["from"])
            operation["to"] = mask_requisites(operation["to"])
        else:
            operation["to"] = mask_requisites(operation["to"])

# применение функции форматированного вывода к каждой операции через цикл
    for operation in formatted_date_operations:
        print(output_operations_history(operation))


filename = '/home/natalya/PycharmProjects/course_work_project/src/operations.json'
get_operations_history(filename)
