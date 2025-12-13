from app import add

def test_add():
  assert add(5,6) == 11

def test_add2():
  assert add(5,6) != 10
