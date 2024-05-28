import json

with open('config.json') as f:
    config = json.load(f)

# You need to add the following keys to a config.json file:
ABSOLUTE_PROJECT_PATH = config.get('PROJECT_DIR')
ABSOLUTE_SUB_DIR_PATH = config.get('SUB_DIR')
DIRECTORIES = config.get('DIRECTORIES')
EXCLUDED_DIRECTORIES = config.get('EXCLUDED_DIRECTORIES')
FILE_NAME = config.get('FILE_NAME')