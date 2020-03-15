import os
import subprocess

def directory(file):
    return "/".join(file.split("/")[:-1])

def filename(file):
    return file.split("/")[-1]

def tape_mkdir(tape_directory):
    # Without the umask, hsi defaults to 077 (group+other are prohibited).
    # Since this module is being designed to help a collaboration backup data, I've set it to 007 (user+group free; others prohibited).
    result = subprocess.call(["hsi", "-P", "umask 007; mkdir -p {}".format(tape_directory)])
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
        output = subprocess.check_output(["hsi", "-P", "ls", "-l", tape_file]).decode('UTF-8').split()

        print(output)
        output = output[1:] # Throw away the first line that corresponds to the prompt.

        # Parse ls -l info:
        size = output[4]
        date = output[5:8]
        return size, date
    except:
        raise ValueError("hsi -P ls -l {} does not exit successfully.".format(tape_file))

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
    return tape_mkdir(tape_directory)


def cput(disk_file, tape_file, log_file=subprocess.DEVNULL):
    ensure_path_exists(tape_file)

    disk_path=directory(disk_file)
    tape_path=directory(tape_file)

    # Without the umask, hsi defaults to 077 (group+other are prohibited).
    # Since this module is being designed to help a collaboration backup data, I've set it to 007 (user+group free; others prohibited).
    # Also, hsi doesn't understand absolute paths.  Hence the lcd; cd; business.
    command = ["hsi", "-P", "umask 007; lcd {}; cd {}; cput {}".format(disk_path, tape_path, filename(disk_file))]
    print(command)
    return subprocess.call(command)

# cget only retrieves if file does not exist on disk
def cget(disk_path, tape_file, log_file=subprocess.DEVNULL):
    subprocess.call(["hsi", "-P", "lcd {}; cget {}".format(disk_path, tape_file)], stdout=log_file, stderr=subprocess.STDOUT)

# get will overwrite disk file with tape file; NOTE - it will update the time stamp of disk file to NOW
def get(disk_path, tape_file, log_file=subprocess.DEVNULL,preserve_time=True):
    if preserve_time:
        subprocess.call(["hsi", "-P", "lcd {}; get -p {}".format(disk_path, tape_file)], stdout=log_file, stderr=subprocess.STDOUT)
    else:
        subprocess.call(["hsi", "-P", "lcd {}; get {}".format(disk_path, tape_file)], stdout=log_file, stderr=subprocess.STDOUT)
