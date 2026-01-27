"""
colors מודול
============
צבעים לפלט בטרמינל
"""

# קודי צבע ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_success(message):
    """מדפיס הודעה בירוק"""
    print(f"{GREEN}{message}{RESET}")


def print_error(message):
    """מדפיס הודעה באדום"""
    print(f"{RED}{message}{RESET}")


def print_result(message):
    """מדפיס תוצאה בכחול"""
    print(f"{BLUE}{message}{RESET}")
