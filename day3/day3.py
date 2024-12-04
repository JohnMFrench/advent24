import re

with open('input3.txt') as f:
    s = f.read()
    print(s)

    p = r"mul\(\d+,\d+\)"
    m = re.findall(p, s)
    print(m)
