import os
import pwd

def get_home_path():
    return os.path.expanduser('~')
