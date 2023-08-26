from utils import read_file, filter_operations, sorted_operations_by_date, the_result

PATH = "operations.json"


def main(path):
    data = read_file(path)
    executed_operations = filter_operations(data)
    sorted_operations = sorted_operations_by_date(executed_operations)
    for i in range(5):
        print(the_result(sorted_operations[i]))


if __name__ == '__main__':
    main(PATH)
