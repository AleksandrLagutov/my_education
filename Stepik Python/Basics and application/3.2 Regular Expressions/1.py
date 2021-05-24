import re
import sys
pattern = r"(.*cat){2,}"
for line in sys.stdin:
    line = line.rstrip()
    inc = re.search(pattern, line)
    if inc:
        print(line)
