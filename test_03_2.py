# https://adventofcode.com/2020/day/3#part2

slopes = [
  (1,1), (3,1), (5,1), (7,1), (1,2)
]

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    map = [line.strip() for line in fh.readlines()]
    res = 1
    length = len(map[0])
    height = len(map)
    for slope in slopes:
      count, top, left = (0, 0, 0)
      while top < height:
        if map[top][left%length] == '#':
          count += 1
        top, left = (top + slope[1], left + slope[0])
    res *= count
  return res

def test_answer1():
  assert func('samples/03.1') ==  336
    
def test_answer2():
  assert func('samples/03.2') == 6419669520
