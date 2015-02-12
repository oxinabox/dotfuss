import config

import glob
import os.path as path

import sys

class states(object):
    LINKED =            config.bcolors.OKGREEN +  "[CONTROLLED] "
    SAME_NAME_NOT_LINKED = config.bcolors.FAIL +  "[CONFLICTED] "
    UNCONTROLLED =      config.bcolors.WARNING +  "[UNCONTROLLED] "
    

def status(include=".*", exclude="*.swp"):
    def get_files(fpath):
        def get_interior_name(exterior_filename):
            return exterior_filename[len(fpath):]

        included = glob.glob(path.join(fpath,include))
        excluded = glob.glob(path.join(fpath,exclude))
        
        files = set(included) - set(excluded)
        return set(map(get_interior_name, files))
    

    home_files   = get_files(config.HOME)
    castle_files = get_files(config.CASTLE_PATH)
    
    print("\nLink Status\n" + 10*"-")
   
    file_status = {}
    for filename in home_files.intersection(castle_files):
        if path.samefile(path.join(config.CASTLE_PATH, filename),
                         path.join(config.HOME, filename)):
            file_status[filename] = states.LINKED
        else: file_status[filename] = states.SAME_NAME_NOT_LINKED 

    for filename in home_files - castle_files:
        file_status[filename] = states.UNCONTROLLED
    
    return file_status


def print_status():
    for (filename, state) in sorted(status().items()):
        print state+filename




