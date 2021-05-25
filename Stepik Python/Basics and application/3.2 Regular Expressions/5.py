import re
import sys

for line in sys.stdin:
    line = line.strip()
    #if re.search(r"human", line):
    print(re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line, flags=re.IGNORECASE))

