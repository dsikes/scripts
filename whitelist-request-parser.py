import sys
import json

try:
    wlr = json.loads(sys.argv[1])
except Exception as err:
    print(err)
    sys.exit(1)

print(wlr)