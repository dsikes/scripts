import os
# import fileinput
import yaml
ansible_workspace_dir = "%s/ansible-code" % (os.getcwd())


def get_yaml_content(f):
    with open(f, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def set_yaml_content(f, d):
    with open('result.yml', 'w') as stream:
        try:
            yaml.dump(d, stream, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)

f = "%s/%s" % (ansible_workspace_dir, 'wordpress-nginx/site.yml')

yc = get_yaml_content(f)
print(yc)
yc["newkey"] = "newval"

sc = set_yaml_content(f, yc)