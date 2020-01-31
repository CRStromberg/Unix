#import os 
  
#path = "."
#dir_list = os.listdir(path) 
#dir_list_stat = os.stat(path)

#print("Files and directories in '", path, "' :")  
  
#print(dir_list) 
#print(dir_list_stat)

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

list_files