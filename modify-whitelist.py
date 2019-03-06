import os
# import fileinput
import yaml
ansible_workspace_dir = "%s/ansible-code" % (os.getcwd())


def get_yaml_content(f):
    with open(f, 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)


yc = get_yaml_content("%s/%s" % (ansible_workspace_dir, 'wordpress-nginx/site.yml'))
print(yc)