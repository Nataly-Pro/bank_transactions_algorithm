from src import utils
from os import path


def test_get_operations_from_file():
    expected = [{'id': 441945886,
             'state': 'EXECUTED',
             'date': '2019-08-26T10:50:58.294041',
             'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'},
             {'id': 41428829,
             'state': 'EXECUTED',
             'date': '2019-07-03T18:35:29.512364',
             'description': 'Перевод организации',
             'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'}]

    filename = path.join('.', 'file.json')
    assert utils.get_operations_from_file(filename) == expected


def test_sort_operations_by_date():
    data = [{"id": 594226727,
             "date": "2019-04-04T23:20:05.206878"},
            {},
            {"id": 147815167,
             "date": "2020-08-26T10:50:58.294041"}]

    expected = [{"id": 147815167,
                 "date": "2020-08-26T10:50:58.294041"},
                 {"id": 594226727,
                 "date": "2019-04-04T23:20:05.206878"}]
    assert utils.sort_operations_by_date(data) == expected


def test_get_some_executed_operations():
    data = [{"id": 594226727,
             "state": "CANCELED"},
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
                 "state": "EXECUTED"}]
    assert utils.get_some_executed_operations(data) == expected


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
