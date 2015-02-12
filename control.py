import sys
import state
import config

import os
import os.path as path
import shutil

def take_control_of_file(filepath):
    print filepath
    actual_file = path.realpath(filepath)    
    assert(path.isfile(actual_file))


    original_filepath = actual_file

    path_in_home = path.relpath(actual_file, config.HOME)
     

    destination = path.realpath(path.join(config.CASTLE_PATH, path_in_home))
    destination_folder = path.dirname(destination)
    if not os.path.exists(destination_folder):
        os.mkdirs(destination_folder)

    shutil.move(actual_file, config.CASTLE_PATH)
    actual_file = destination
    assert(path.isfile(actual_file))
    
    os.symlink(actual_file, original_filepath);
    print config.bcolors.OKGREEN + "Linked %s --> %s" % (original_filepath, actual_file)
    assert(path.samefile(original_filepath, actual_file ));


def take_control_of_dir(dirpath):
    for root, _, filenames in os.walk(dirpath):
        for filename in filenames:
            filepath = path.join(root,filename)
            take_control_of_file(filepath)


def take_control(*args):
    for filepath in args:
        if path.isdir(filepath):
            take_control_of_dir(filepath)
        else:
            take_control_of_file(filepath)

