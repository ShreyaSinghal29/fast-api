import requests
import pytest

@pytest.mark.parametrize("url, expected", [
    ("http://127.0.0.1:8000/add/1/2", 3),
    ("http://127.0.0.1:8000/add/-1/1", 0),
    ("http://127.0.0.1:8000/multiply/3/4", 12),
    ("http://127.0.0.1:8000/multiply/0/5", 0),
])
def test_api(url, expected):
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["result"] == expected
