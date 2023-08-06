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
