import os 
  
path = "/home/chris"
dir_list = os.listdir(path) 
dir_list_stat = os.stat(path)

print("Files and directories in '", path, "' :")  
  
print(dir_list) 
print(dir_list_stat)
