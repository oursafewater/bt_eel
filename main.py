"""
bt_eel

Brandon Taylor, PE
December, 2018

"""

import os
import shutil
import errno
import random

# import eel
# eel.init('web')


INPUT_FOLDER = '\\media\\pi\\'
OUTPUT_FOLDER = '\\home\\pi\\DVDBackups\\'



# @eel.expose
def print_string(x):
    print('String Provided: {}'.format(x))


# @eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        return random.choice(os.listdir(folder))
    else:
        return 'Not valid folder'

def timestamp():

    from datetime import datetime

    # Create TimeStamp (eg. 1201_1850)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)

    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute

    timestamp = month + day + '_' + hour + minute

    return timestamp

def copy(src, dest):

    try:
        shutil.copy(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)



# @eel.expose
def backup_drive(input, output):

    # Determine If Directories Exist
    inputqc = os.path.isdir(input)
    outputqc = os.path.isdir(output)

    # Build Final Folder Name
    outputfinal = output + timestamp()

    # Copy Files If Directory Does Not Already Exist
    if not os.path.exists(outputfinal):
        copy(input, outputfinal)
    else:
        print('Directory Already Exists.  Wait a Minute (literally).')


def main():
    # eel.start('index.html')
    # eel.start('file_access.html', size=(320, 120))

    # eel.start('backup_drive.html', size=(360, 120))

    val = backup_drive(INPUT_FOLDER, OUTPUT_FOLDER)



if __name__ == '__main__':
    main()
