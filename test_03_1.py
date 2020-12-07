# https://adventofcode.com/2020/day/3

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    return sum([
      1 for i, line in enumerate(fh.readlines())
      if line[3*i%len(line)] == '#'
    ])

def test_answer1():
  assert func('samples/03.1') ==  7
    
def test_answer2():
  assert func('samples/03.2') == 580
