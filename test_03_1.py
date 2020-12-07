# https://adventofcode.com/2020/day/3

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    map = [x for x in fh.readlines()]
    top, left, count = (0,0,0)
    while top < len(map):
      if map[top][left] == '#':
        count += 1
      top, left = (top + 1, (left + 3)%len(map[top]))
    return count

def test_answer1():
  assert func('samples/03.1') ==  7
    
def test_answer2():
  assert func('samples/03.2') == 580
