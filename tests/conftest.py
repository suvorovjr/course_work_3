import pytest


@pytest.fixture
def fixture_filter_operations():
    return [{"id": 863064926,
             "state": "EXECUTED",
             "date": "2019-12-08T22:46:21.935582",
             "operationAmount": {
                 "amount": "41096.24",
                 "currency": {
                     "name": "USD",
                     "code": "USD"
                 }
             },
             "description": "Открытие вклада",
             "to": "Счет 90424923579946435907"
             },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }]


@pytest.fixture
def fixture_one_operation():
    return {
        "id": 542678139,
        "state": "EXECUTED",
        "date": "2018-10-14T22:27:25.205631",
        "operationAmount": {
            "amount": "90582.51",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 2256483756542539",
        "to": "Счет 78808375133947439319"
    }
