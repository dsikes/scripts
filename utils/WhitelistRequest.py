import yaml

class WhitelistRequest():

    def __init__(self, stream):
        """ sets content property of a whitelist request object """
        try:
            self.content = json.load(stream)
        except Exception as err:
            raise (str(err))
        
    #### PRIVATE METHODS #####
    
    def _get_yaml_content(self, f):
        with open(f, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                
    def _set_yaml_content(self, f, d):
        if os.path.isfile(f):
            os.remove(f)
        
        with open(f, 'w+') as stream:
            try:
                yaml.dump(d, stream, default_flow_style=False)
            except yaml.YAMLError as exc:
                print(exc)
    

    #### PUBLIC METHODS ######
    
    def get_ip_blocks():

        if 'ipblocks' in self.content:
            self.ipblocks = self.content['ipblocks']
            return
        
        raise Exception("no ipblocks in whitelist request")
    
    
    def get_service_now_ticket_id():

        if 'service_now_ticket_id' in self.content:
            self.service_now_ticket_id = self.content['service_now_ticket_id']
            return
        
        raise Exception("no service now ticket id in whitelist request")
    
    def get_services():

        if 'services' in self.content:
            self.services = self.content['services']
            return

        raise Exception("no services in whitelist request")
    