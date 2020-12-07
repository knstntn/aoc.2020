# https://adventofcode.com/2020/day/2

import utils.policy as policy

def is_valid(line: str) -> bool:
  count = 0
  policy, pwd = policy.parse(line)
  for c in pwd:
    if c == policy.char:
      count += 1
  return policy.left <= count and policy.right >= count

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    return sum([1 for line in fh.readlines() if is_valid(line)])

def test_answer1():
  assert func('samples/02.1') ==  2
    
def test_answer2():
  assert func('samples/02.2') == 580
