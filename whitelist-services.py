import sys
from utils.WhitelistRequest import WhitelistRequest


# The white list request comes into this script via Jenkins as a sys argument.
# This script is designed to print the error and exit if any of the data is 
# malformed to fail the job.

wlr = WhitelistRequest(sys.argv[1])

print("============ SERVICE NOW =================")
print(wlr.service_now_ticket_id)


print("============ IP BLOCKS =================")
print(wlr.ipblocks)

print("============ SERVICES =================")
print(wlr.services)


# try:

# except Exception as err:
#     print(err)
#     sys.exit(1)

