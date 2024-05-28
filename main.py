from counters_alert import add_counters_alert
from config import DIRECTORIES, EXCLUDED_DIRECTORIES, ABSOLUTE_PROJECT_PATH, ABSOLUTE_SUB_DIR_PATH, FILE_NAME

APP_NAME = 'webanalyticsws'


def main():
    add_counters_alert(DIRECTORIES, EXCLUDED_DIRECTORIES, ABSOLUTE_PROJECT_PATH, ABSOLUTE_SUB_DIR_PATH, FILE_NAME,
                       APP_NAME, 500)


if __name__ == "__main__":
    main()
