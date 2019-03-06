import json
import yaml

class WhitelistRequest():

    def __init__(self, stream):
        """ sets content property of a whitelist request object """
        self.content = json.loads(stream)
        self._get_ip_blocks()
        self._get_services()
        self._get_service_now_ticket_id()

    #### PRIVATE METHODS ######
    
    def _get_ip_blocks(self):

        if 'ipblocks' in self.content:
            self.ipblocks = self.content['ipblocks']
            return
        
        raise Exception("no ipblocks in whitelist request")
    
    
    def _get_service_now_ticket_id(self):

        if 'service_now_ticket_id' in self.content:
            self.service_now_ticket_id = self.content['service_now_ticket_id']
            return
        
        raise Exception("no service now ticket id in whitelist request")
    
    def _get_services(self):

        if 'services' in self.content:
            self.services = self.content['services']
            return

        raise Exception("no services in whitelist request")
    
    #### PUBLIC METHODS #####
    
    def get_yaml_content(self, f):
        with open(f, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                
    def set_yaml_content(self, f, d):
        if os.path.isfile(f):
            os.remove(f)
        
        with open(f, 'w+') as stream:
            try:
                yaml.dump(d, stream, default_flow_style=False)
            except yaml.YAMLError as exc:
                print(exc)