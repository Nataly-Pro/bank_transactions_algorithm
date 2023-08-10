from os import path
from pathlib import Path
from utils import get_operations_from_file, sort_operations_by_date,\
    get_executed_operations, change_operation_date, mask_requisites,\
    output_operations_history

ROOT_PATH = Path(__file__).parent.parent
SRC_PATH = Path.joinpath(ROOT_PATH, "src")
OPERATION_JSON = Path.joinpath(SRC_PATH, "operations.json")

def get_operations_history(json_file):
    operations = get_operations_from_file(json_file)
    executed_operations = get_executed_operations(operations)
    sorted_operations = sort_operations_by_date(executed_operations)
    formatted_date_operations = change_operation_date(sorted_operations)

# перебор операций в цикле для маскировки платежных реквизитов
    for operation in formatted_date_operations:
        if operation["description"] != "Открытие вклада":
            operation["from"] = mask_requisites(operation["from"])
            operation["to"] = mask_requisites(operation["to"])
        else:
            operation["to"] = mask_requisites(operation["to"])

# применение функции форматированного вывода к каждой операции через цикл
    history = []
    for operation in formatted_date_operations:
        history.append(output_operations_history(operation))
    return '\n'.join(history)


print(get_operations_history(OPERATION_JSON))
