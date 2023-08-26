from utils import read_file, executed_operations

PATH = "operations.json"

data = read_file(PATH)
print(executed_operations(data))