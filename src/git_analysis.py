import os
import sys


def clone_project(full_name, folder_name):
    print("############# Cloning Project ################", file=sys.stdout)
    os.system(f"git clone https://github.com/{full_name}.git " + folder_name + "/" + full_name.split("/")[1])
    print("############# Cloning Complete ###############", file=sys.stdout)
