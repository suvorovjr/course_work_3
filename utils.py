import json
import datetime


def read_file(filename):
    """
    открывает файл
    :param filename:путь к файлу
    :return: содержимое файла
    """
    with open(filename, "rt", encoding="utf-8") as file:
        return json.loads(file.read())


def filter_operations(data):
    """
    фильрует успешные операции
    :param data:данные файла
    :return:отфильтрованный список
    """
    executed_operations = [operation for operation in data if operation.get("state") == "EXECUTED"]
    return executed_operations


def sorted_operations_by_date(executed_operations):
    """
    сортировка операций по дате
    :param executed_operations: список успешных операций
    :return: отсортированный список операций
    """
    sorted_operations = list(sorted(executed_operations, key=lambda operation: operation['date'], reverse=True))[:5]
    return sorted_operations


def converte_date(date):
    """
    приводит дату к правильному формату
    :param date:дата в исходном формате
    :return:нужный формат даты
    """
    date_ = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime.datetime.strftime(date_, '%d.%m.%Y')


def format_card(data):
    """
    приводит к нужному формату данные получателя или отправителя
    :param data:данные отправителя или получателя в исходном формате
    :return:нужный формат отправителя или получаателя
    """
    if data.startswith("Счет"):
        return f"Счет **{data[-4:]}"
    else:
        name_card = "".join([letter for letter in data if not letter.isdigit()])
        number_card = "".join([num for num in data if num.isdigit()])
        return f"{name_card}{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def the_result(data):
    """
    конечный вывод данных
    :param data:данные об операции
    :return:данные в нужном формате
    """
    date_ = converte_date(data["date"])
    description = data["description"]
    to_ = format_card(data["to"])
    if data.get("from"):
        from_ = format_card(data["from"])
    else:
        from_ = ""
    amount = data["operationAmount"]["amount"]
    name = data["operationAmount"]["currency"]["name"]
    return f"{date_} {description}\n" \
           f"{from_} -> {to_}\n" \
           f"{amount} {name}\n"
