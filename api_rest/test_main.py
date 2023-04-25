from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

def test():
    print("Dorian ta mère")
    assert 1 == 1