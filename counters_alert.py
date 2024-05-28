import os

from ruamel.yaml import YAML


def add_counters_alert(directories, excluded_directories, absolute_project_path, absolute_sub_dir_path, file_name,
                       app_name, threshold):
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
            'alert': f'High number of events not processed in {app_name}',
            'annotations': {
                'description': f'This alert is triggered when the number of events not processed during the last 5 minutes is more than {threshold}',
                'summary': 'High number of not processed events.',
            },
            'expr': f'sum(increase(unknown_events_count{{application_info_id="{app_name}"}}[5m]) + increase(invalid_events_count{{application_info_id="{app_name}"}}[5m]) + increase(invalid_content_count{{application_info_id="{app_name}"}}[5m])) or on() vector(0) >= {threshold}',
            'labels': {
                'severity': 'warning',
                'app_group': 'squids',
                'receiver': receiver,
            },
        }

        # Construct the file path
        file_path = os.path.join(absolute_project_path, absolute_sub_dir_path, directory, file_name)

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