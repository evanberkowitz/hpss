import os
import subprocess

def directory(file):
    return "/".join(file.split("/")[:-1])

def tape_mkdir(tape_directory):
    result = subprocess.call(["hsi", "mkdir", "-p", tape_directory])
    if result == 0:
        return result
    else:
        raise ValueError("Could not create directory {}\nReturn value {}".format(tape_directory, result))
    return result

def disk_mkdir(disk_directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

def tape_info(tape_file):
    try:
        output = subprocess.check_output(["hsi", "-P", "ls", "-l", "--time-style", "long-iso", tape_file]).decode('UTF-8').split()
    except:
        raise ValueError("hsi -P ls -l {} does not exit successfully.".format(tape_file))

    output = output[1:] # Throw away the first line that corresponds to the prompt.
    
    # Parse ls -l info:
    size = output[4]
    date = output[5:8]
    return size, date

def disk_info(disk_file):
    try:
        output = subprocess.check_output(["ls", "-l", "--time-style", "long-iso", disk_file]).decode('UTF-8').split()
    except:
        raise ValueError("ls -l {} does not exist successfully.".format(disk_file))

    # Parse ls -l info:
    size = output[4]
    date = output[5:8]
    return size, date

def ensure_path_exists(tape_file):
    tape_directory = "/".join(tape_file.split("/")[:-1])
    tape_mkdir(tape_directory)
    

def cput(disk_file, tape_file, log_file=subprocess.DEVNULL):
    mkdir(tape_directory)
    return subprocess.call(["hsi", "cput", disk, tape], stdout=log_file, stderr=subprocess.STDOUT)
    

def cget(disk, tape, log_file=subprocess.DEVNULL):
    subprocess.call(["hsi", "cget", tape, disk], stdout=log_file, stderr=subprocess.STDOUT)

def update_file(disk_file, tape_file):
    
    try:
        tape_size, tape_date = tape_info(tape_file)
    except:
        tape_mkdir(directory(tape_file))
        return cput(disk_file, tape_file)
        
    disk_size, disk_date = disk_info(disk_file)
    
    # Compare dates, cput if disk is newer.
    ...

def update_dir(disk_dir, tape_dir):
    # Loop over each file in disk_dir and update_file
    ...

def update(disk, tape):
    # Dispatch to _file or _dir based on disk target type.
    ...