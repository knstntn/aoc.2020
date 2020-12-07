# https://adventofcode.com/2020/day/3

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    map = [line for line in fh.readlines()]
    length = len(map[0])
    height = len(map)
    count, down, right = (0, 0, 0)
    while height > down:
      if map[top][right%length] == '#':
        count += 1
      down, right = (down + 1, right + 3)
    return count

def test_answer1():
  assert func('samples/03.1') ==  7
    
def test_answer2():
  assert func('samples/03.2') == 580
