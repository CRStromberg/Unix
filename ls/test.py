
# determine size of a given folder in MBytes
import os
# pick a folder you have ...
folder = '/home'
folder_size = 0
for (path, dirs, files) in os.walk(folder):
    for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
print(folder_size)
