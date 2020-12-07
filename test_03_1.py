# https://adventofcode.com/2020/day/3

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    map = [x for x in fh.readlines()]
    length = len(map[0])
    slope = (1,3)
    top, left, count = (0,0,0)
    while top < len(map):
      if map[top][left%length] == '#':
        count += 1
      top, left = (top + slope[0], left + slope[1])
    return count

def test_answer1():
  assert func('samples/03.1') ==  7
    
def test_answer2():
  assert func('samples/03.2') == 580
