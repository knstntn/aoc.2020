# https://adventofcode.com/2020/day/2

import typing as typing

class Policy(typing.NamedTuple):
  min: int
  max: int
  char: str

def parse(line: str) -> typing.Tuple[Policy, str]:
  policy, _, pwd = line.partition(':')
  min, _, rest = policy.partition('-')
  max, _, char = rest.partition(' ')
  return (Policy(min=int(min), max=int(max), char=char.strip()), pwd.strip())

def is_valid(line: typing.Tuple[Policy, str]) -> bool:
  count = 0
  policy, pwd = line
  for c in pwd:
    if c == policy.char:
      count += 1
  return policy.min <= count and policy.max >= count

def func(filename: str) -> int:
  with open(filename,'r') as fh:
    return sum([1 for line in fh.readlines() if is_valid(parse(line))])

def test_answer1():
  assert func('samples/02.1') ==  2
    
def test_answer2():
  assert func('samples/02.2') == 1
