from errors_alert import add_errors_alert
from config import DIRECTORIES, EXCLUDED_DIRECTORIES, ABSOLUTE_PROJECT_PATH, ABSOLUTE_SUB_DIR_PATH

APP_NAME = 'webanalyticsws'


def main():
    add_errors_alert(DIRECTORIES, EXCLUDED_DIRECTORIES, ABSOLUTE_PROJECT_PATH, ABSOLUTE_SUB_DIR_PATH, APP_NAME)


if __name__ == "__main__":
    main()
