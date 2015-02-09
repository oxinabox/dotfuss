import config

import glob
import os.path

def link_status(rel_path, include".*", exclude="*.swp"):
    def get_files(path):
        included = glob.glob(os.path.join(path,include))
        excluded = glob.glob(os.path.join(path,include))
        return set(included) - set(excluded)

    home_files   = get_files(config.HOME)
    castle_files = get_files(config.CASTLE_PATH)

    
    
    

if __name__ =="__main__":
    list_all(config.home)
