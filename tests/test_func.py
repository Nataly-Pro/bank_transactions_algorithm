from src.func import get_operations_history


def test_get_operations_history():
    assert get_operations_history('/home/natalya/PycharmProjects/course_work_project/tests/file.json') == None
