import os
import sys
import re

SLUG_REGEX = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
service_name = "{{ cookiecutter.service_name }}"

if not re.match(SLUG_REGEX, service_name):
    print("Error: {0} is not a valid slug format".format(service_name))
    sys.exit(1)

