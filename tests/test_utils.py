from os import path
from pathlib import Path
import sys
import utils

sys.path.append(path.abspath(path.join('src', 'utils')))

ROOT_PATH = Path(__file__).parent.parent
TESTS_PATH = Path.joinpath(ROOT_PATH, "tests")
FILE_JSON = Path.joinpath(TESTS_PATH, "file.json")


def test_get_operations_from_file():
    expected = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                 'to': 'Счет 64686473678894779589'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                 'to': 'Счет 35383033474447895560'}]

    assert utils.get_operations_from_file(FILE_JSON) == expected


def test_sort_operations_by_date():
    data = [{"id": 594226727,
             "date": "2019-04-04T23:20:05.206878"},
            {"id": 147815167,
             "date": "2020-08-26T10:50:58.294041"}]

    expected = [{"id": 147815167,
                 "date": "2020-08-26T10:50:58.294041"},
                {"id": 594226727,
                 "date": "2019-04-04T23:20:05.206878"}]
    assert utils.sort_operations_by_date(data) == expected


def test_get_executed_operations():
    data = [{"id": 594226727,
             "state": "CANCELED"},
            {},
            {"id": 147815167,
             "state": "EXECUTED"},
            {"id": 716496732,
             "state": "EXECUTED"},
            {"id": 147815167,
             "state": "EXECUTED"},
            {"id": 518707726,
             "state": "EXECUTED"},
            {"id": 649467725,
             "state": "EXECUTED"},
            {"id": 782295999,
             "state": "EXECUTED"}]

    expected = [{"id": 147815167,
                 "state": "EXECUTED"},
                {"id": 716496732,
                 "state": "EXECUTED"},
                {"id": 147815167,
                 "state": "EXECUTED"},
                {"id": 518707726,
                 "state": "EXECUTED"},
                {"id": 649467725,
                 "state": "EXECUTED"},
                {"id": 782295999,
                 "state": "EXECUTED"}]
    assert utils.get_executed_operations(data) == expected


def test_change_operation_date():
    data = [{"id": 594226727,
             "date": "2019-04-04T23:20:05.206878"},
            {"id": 147815167,
             "date": "2020-08-26T10:50:58.294041"}]

    expected = [{"id": 594226727,
                 "date": "4.4.2019"},
                {"id": 147815167,
                 "date": "26.8.2020"}]
    assert utils.change_operation_date(data) == expected


def test_mask_requisites():
    assert utils.mask_requisites("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert utils.mask_requisites("Счет 64686473678894779589") == "Счет **9589"


def test_output_operations_history():
    data = {'id': 441945886,
            'state': 'EXECUTED',
            'date': '2019-08-26T10:50:58.294041',
            'operationAmount': {'amount': '31957.58',
                                'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Перевод организации',
            'from': 'Maestro 1596 83** **** 5199',
            'to': 'Счет **9589'}

    expected = ('2019-08-26T10:50:58.294041 Перевод организации\n'
                'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                '31957.58 руб.\n')

    assert utils.output_operations_history(data) == expected
