# https://adventofcode.com/2020/day/1

def func(filename: str) -> int:
  sum = 2020
  with open(filename,'r') as fh:
    nums = [int(line) for line in fh.readlines()]
    res = set()
    for num in nums:
      if num in res:
        return num * (sum - num)
      res.add(sum - num)
  return 0

def test_answer1():
    assert func('inputs/01.1') ==  514579
    
print(func('inputs/01.2'))
