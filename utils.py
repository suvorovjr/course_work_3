import json

def read_file(filename):
    with open(filename, "rt", encoding="utf-8") as file:
        return json.loads(file.read())


def executed_operations(data):
    filter_operations = [operation for operation in data if operation.get("state") == "EXECUTED"]
    return filter_operations