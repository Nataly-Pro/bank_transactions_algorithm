import pytest
from src import utils


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
