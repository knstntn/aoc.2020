import typing as typing

class Policy(typing.NamedTuple):
  left: int
  right: int
  char: str

def parse(line: str) -> typing.Tuple[Policy, str]:
  policy, _, pwd = line.partition(':')
  left, _, rest = policy.partition('-')
  right, _, char = rest.partition(' ')
  return (Policy(left=int(left), right=int(right), char=char.strip()), pwd.strip())
