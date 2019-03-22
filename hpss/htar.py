import os
import subprocess
from . import hsi

def cvf(disk_dir, tape_file, log_file=subprocess.DEVNULL):
    hsi.ensure_path_exists(tape_file)
    tape_path=hsi.directory(tape_file)
    
    command = ["htar", "-H", "umask=007", "-cvf", tape_file, disk_dir] 
    print(command)
    return subprocess.call(command)

