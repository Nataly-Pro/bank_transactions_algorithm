from pathlib import Path

ROOT_PATH = Path(__file__).parent
SRC_PATH = Path.joinpath(ROOT_PATH, "src")
TEST_FILE_PATH = Path.joinpath(ROOT_PATH, "tests", "file.json")
OPERATION_JSON = Path.joinpath(SRC_PATH, "operations.json")
