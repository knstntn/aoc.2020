# https://adventofcode.com/2020/day/2#part2

import utils.policy as PolicyUtils

def is_valid(line: str) -> bool:
  count = 0
  policy, pwd = PolicyUtils.parse(line)
  is_left_match = pwd[policy.left - 1] == policy.char
  is_right_match = pwd[policy.right - 1] == policy.char
  return (is_left_match is True and is_right_match is False) or (is_left_match is False and is_right_match is True)

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    return sum([1 for line in fh.readlines() if is_valid(line)])

def test_answer1():
  assert func('samples/02.1') ==  1
    
def test_answer2():
  assert func('samples/02.2') == 580
