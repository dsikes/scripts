import yaml

def get_yaml_content(f):
    with open(f, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

whitelist = get_yaml_content("/wlr/wlr.yaml")

print(whitelist)