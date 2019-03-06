import sys
import os
from utils.WhitelistRequest import WhitelistRequest

# for dev purposes only...
ansible_workspace_dir = "%s/ansible-code" % (os.getcwd())
f = "%s/%s" % (ansible_workspace_dir, 'wordpress-nginx/site.yml')

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


wlr.get_yaml_content(f)
for ip in wlr.ipblocks:
    wlr.fcontent[0]["roles"].append(ip)

wlr.set_yaml_content(f)

# try:

# except Exception as err:
#     print(err)
#     sys.exit(1)

