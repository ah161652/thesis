import os
import pwd


# def get_username():
#     return pwd.getpwuid(os.getuid())[0]


# def get_unique_machine_id():
#     with open("/etc/machine-id") as f :
#         id = f.read()
#         if('\n' in id):
#             id = id.replace('\n', '')
#
#     return id


def get_home_path():
    return os.path.expanduser('~')
