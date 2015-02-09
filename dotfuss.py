import config

import glob
import os.path as path

def link_status(include=".*", exclude="*.swp"):
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
    print('\n')  
   
    print home_files
    print castle_files

    for filename in home_files.intersection(castle_files):
        print filename
        if path.samefile(path.join(config.CASTLE_PATH, filename),
                         path.join(config.HOME, filename)):
            print(':-)')
            print config.bcolors.OKGREEN +  "[LINKED] " + filename
        else: print config.bcolors.FAIL +  "[BORKED] " + filename
    
    print('\n')   
    for filename in home_files - castle_files:
        print config.bcolors.WARNING +  "[UNCONTROLLED] "+filename
 

if __name__ =="__main__":
    link_status()
