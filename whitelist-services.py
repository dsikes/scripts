import sys
import json
from utils.WhitelistRequest import WhitelistRequest


# The white list request comes into this script via Jenkins as a sys argument.
# This script is designed to print the error and exit if any of the data is 
# malformed to fail the job.
try:
    wlr = WhitelistRequest(sys.argv[1])
    print(wlr.get_ip_blocks())
except Exception as err:
    print(err)
    sys.exit(1)
