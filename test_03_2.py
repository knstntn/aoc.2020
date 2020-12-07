# https://adventofcode.com/2020/day/3#part2

slopes = [
  (1,1), (3,1), (5,1), (7,1), (1,2)
]

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    map = [x.strip() for x in fh.readlines()]
    res = 1
    for slope in slopes:
      res *= sum([
        1 for i, line in enumerate(map)
        if i%slope[1] == 0 and line[slope[0]*i%len(line)] == '#'
      ])
    return res

def test_answer1():
  assert func('samples/03.1') ==  336
    
def test_answer2():
  assert func('samples/03.2') == 6419669520
