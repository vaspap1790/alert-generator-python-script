import os

from ruamel.yaml import YAML


def add_errors_alert(directories, excluded_directories, absolute_project_path, absolute_sub_dir_path, app_name):
    # Create a YAML object
    yaml = YAML()
    yaml.indent(sequence=4, offset=2)
    yaml.width = 10000

    # Iterate over all directories
    for directory in directories:
        # Skip excluded directories
        if directory in excluded_directories:
            continue

        # Replace hyphen with underscore in directory name
        receiver = directory.replace('-', '_')

        # Define the alert to be added
        alert = {
            'alert': f'High percentage server error in {app_name}',
            'annotations': {
                'description': 'Maximum number of 5xx errors reached',
                'summary': f'The app is producing too many 5XX errors.',
            },
            'expr': f'(sum(increase(http_server_requests_seconds_count{{application_info_id="{app_name}", uri!~"(/prometheus|/health-check)", status=~"5\\\\d\\\\d"}}[5m])) or on() vector(0))/(sum(increase(http_server_requests_seconds_count{{application_info_id="{app_name}s", uri!~"(/prometheus|/health-check)"}}[5m]))+1)*100 > 5',
            'for': '15m',
            'labels': {
                'severity': 'critical',
                'app_group': 'squids',
                'receiver': receiver,
            },
        }

        # Construct the file path
        file_path = os.path.join(absolute_project_path, absolute_sub_dir_path, directory, 'rules.yml')

        # Load the existing YAML data
        with open(file_path, 'r') as file:
            data = yaml.load(file)

        # Add the alert under 'rules' within 'groups'
        for group in data['groups']:
            if group['name'] == 'Prometheus Rules':
                group['rules'].append(alert)
                break

        # Write the updated YAML data back to the file
        with open(file_path, 'w') as file:
            yaml.dump(data, file)