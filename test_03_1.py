# https://adventofcode.com/2020/day/3

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    data = [x for x in fh.readlines()]
    trees = 0
    slope = (3,1)
    right, down = (3, 0)
    while down < len(data):
        if data[down][right % len(data[0])] == '#':
            trees += 1
        right += slope[0]
        down += slope[1]
    return trees

def test_answer1():
  assert func('samples/03.1') ==  7
    
def test_answer2():
  assert func('samples/03.2') == 580
