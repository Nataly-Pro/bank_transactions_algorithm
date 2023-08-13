from main import get_operations_history
from settings import TEST_FILE_PATH


def test_get_operations_history():
    assert get_operations_history(TEST_FILE_PATH) == \
           ('26.8.2019 Перевод организации\n'
            'Maestro 1596 83** **** 5199 -> Счет **9589\n'
            '31957.58 руб.\n'
            '\n'
            '3.7.2019 Перевод организации\n'
            'MasterCard 7158 30** **** 6758 -> Счет **5560\n'
            '8221.37 USD\n')
