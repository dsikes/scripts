import sys
import json

try:
    wlr = json.loads(sys.argv[1])
except Exception as err:
    print(err)
    sys.exit(1)

print("========================================")
print(wlr)
print("========================================")


print("========================================")
print("SERVICES\n")
print(wlr['services'])


print("IPBLOCKS\n")
print(wlr['ipblocks'])


print("SERVICE NOW TICKET\n")
print(wlr['service_now_ticket_id'])

print("========================================")
