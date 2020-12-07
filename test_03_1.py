# https://adventofcode.com/2020/day/3

def is_valid(line: str) -> bool:
  count = 0
  policy, pwd = PolicyUtils.parse(line)
  for c in pwd:
    if c == policy.char:
      count += 1
  return policy.left <= count and policy.right >= count

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    map = [line for line in fh.readlines()]
    return 0

def test_answer1():
  assert func('samples/03.1') ==  7
    
def test_answer2():
  assert func('samples/03.2') == 580
