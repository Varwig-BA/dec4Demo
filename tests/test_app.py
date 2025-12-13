import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import app

def test_add():
  assert app.add(5,6) == 11

def test_add2():
  assert app.add(5,6) != 10

def test_subtract():
  assert app.subtract(6,5) == 1

def test_subtract2():
  assert app.subtract(5,6) == -1

def test_subtract3():
  assert app.subtract(6,5) != 0

def test_multiply():
  assert app.multiply(2,6) == 12

def test_multiply2():
  assert app.multiply(2,6) != 13

def test_divide():
  assert app.divide(6,2) == 3

def test_divide2():
  assert app.divide(7,2) == 3.5

def test_divide3():
  assert app.divide(7,2) != 3

def test_logarithm():
  assert app.logarithm(4,2) == 2

def test_logarithm2():
  assert app.logarithm(1,10) == 0

def test_square():
  assert app.square(10) == 100

def test_sine():
  assert app.sine(0) == 0

def test_cosine():
  assert app.cosine(0) == 1

def test_sqrt():
  assert app.sqrt(100) == 10

def test_percentage():
  assert app.percentage(2,8) == 25
