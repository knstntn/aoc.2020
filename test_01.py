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
  assert func('samples/01.1') ==  514579
    
def test_answer2():
  asset func('samples/01.2') == -1
