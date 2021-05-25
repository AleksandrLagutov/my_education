import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\b(\w+)\1\b", line):
        print(line)
