import os
import subprocess
from . import hsi

def cvf(disk_dir, tape_file, log_file=subprocess.DEVNULL):
    hsi.ensure_path_exists(tape_file)
    tape_path=hsi.directory(tape_file)
    
    command = ["htar", "-H", "umask=007", "-cvf", tape_file, disk_dir] 
    print(command)
    return subprocess.call(command)

def t(tape_file, log_file=subprocess.DEVNULL):
    try:
        size, date = hsi.tape_info(tape_file)
        print(f"{tape_file} is {size} big and was created on {date}")
    except:
        return -1

    command = ["htar", "-tf", tape_file]
    print(command)
    return subprocess.call(command)

def x(tape_file, log_file=subprocess.DEVNULL):
    try:
        size, date = hsi.tape_info(tape_file)
        print(f"{tape_file} is {size} big and was created on {date}")
    except:
        return -1

    print(f"Working directory in which we are expanding is {os.getcwd()}")
    command = ["htar", "-xf", tape_file]
    print(command)
    return subprocess.call(command)
