import requests
import json


def get(a, b):
    return (json
            .loads(requests
                   .get(f'http://localhost:5000/?a={a}&b={b}')
                   .text))\
        .get('res')


def test_1():
    assert get(10, 5) == 2


def test_2():
    assert get(10, 0) == 'Нельзя делить на ноль'


def test_3():
    assert get(100, 5) == 20
