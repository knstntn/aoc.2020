# https://adventofcode.com/2020/day/1#part2

def func(filename: str) -> int:
  sum = 2020
  with open(filename,'r') as fh:
    nums = [int(line) for line in fh.readlines()]
    for i, num in enumerate(nums):
      res = calc(sum - num, nums, i)
      if res != 0:
        return res * num
    return 0
    
def calc(sum: int, nums: List[int], skip: int) -> int:
  res = set()
    for i, num in enumerate(nums):
      if i == skip:
        continue
        
      if num in res:
        return num * (sum - num)
      res.add(sum - num)
  return 0

def test_answer1():
  assert func('samples/01.1') ==  241861950
    
def test_answer2():
  assert func('samples/01.2') == -1
