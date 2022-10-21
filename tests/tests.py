import requests
import json


def get(a: int, b: int) -> float:
    return (json
            .loads(requests
                   .get(f'http://localhost:5000/?a={a}&b={b}')
                   .text))\
        .get('res')


def test_1() -> None:
    assert get(10, 5) == 2


def test_2() -> None:
    assert get(10, 0) == 'Нельзя делить на ноль'


def test_3() -> None:
    assert get(100, 5) == 20
