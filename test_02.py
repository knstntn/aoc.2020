# https://adventofcode.com/2020/day/1#part2

from typing import List, Optional

def func(filename: str) -> Optional[int]:
  sum = 2020
  with open(filename,'r') as fh:
    nums = [int(line) for line in fh.readlines()]
    for i, num in enumerate(nums):
      res = calc(sum - num, nums, i)
      if res is not None:
        return res * num
    
def calc(sum: int, nums: List[int], skip: int) -> Optional[int]:
  res = set()
  for i, num in enumerate(nums):
    if i == skip:
      continue

    if num in res:
      return num * (sum - num)
    res.add(sum - num)

def test_answer1():
  assert func('samples/01.1') ==  241861950
    
def test_answer2():
  assert func('samples/01.2') == 8446464
