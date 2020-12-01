# https://adventofcode.com/2020/day/1

def func(filename: str) -> num:
  with open(filename,'r') as fh
    lines = [int(line) for line in fh.readlines()]
    print(lines)
    
                  
  return 0

def test_answer1():
    assert func('inputs/01.1') ==  514579
    
print(func('inputs/01.2'))
