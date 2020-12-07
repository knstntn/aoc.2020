# https://adventofcode.com/2020/day/2

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    list = [line for line in fh.readlines()]
  return 2

def test_answer1():
  assert func('samples/02.1') ==  2
    
def test_answer2():
  assert func('samples/02.2') == 1
