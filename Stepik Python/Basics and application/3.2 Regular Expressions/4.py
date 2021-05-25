import re
import sys

for line in sys.stdin:
    line = line.strip()
    #if re.search(r"human", line):
    print(re.sub("human","computer", line))

