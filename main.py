"""
bt_eel

Brandon Taylor, PE
December, 2018

"""
import eel
import os
import random


BACKUP_FOLDER = '\\FILEPATH\\'

eel.init('web')


@eel.expose
def print_string(x):
    print('String Provided: {}'.format(x))


@eel.expose
def pick_file(folder):
    if os.path.isdir(folder):
        return random.choice(os.listdir(folder))
    else:
        return 'Not valid folder'


@eel.expose
def backup_dvd(letter):

    drive_found = os.system("vol %s: 2>nul>nul" % letter) == 0

    if drive_found:
        print('{}:\ Found'.format(letter))


def main():
    # eel.start('index.html')
    # eel.start('file_access.html', size=(320, 120))

    eel.start('backup_dvd.html', size=(360, 120))

    val = backup_dvd('C')
    # print(val)


if __name__ == '__main__':
    main()
