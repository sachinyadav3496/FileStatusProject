#!\usr\bin\env python3
"""
myutils module contains some of the functions and modules used in Lab1 Project

functions:
    get_size(bytes) -> return size in terms of B, KB, MB, GB and TB
    get_list(dir)   -> return a detail list of files exists in dir
            having their name, size, and access / modify time
"""
import os
# used to access file attributes and path related functionality
import time
# to access time related functionality

def get_size(size_bytes):
    """
        return size of a file in B, KB, MB, GB, TB given by bytes
    """
    sizes = ['B', 'kB', 'MB', 'GB', 'TB']
    if size_bytes < 1024:
        return f"{size_bytes}B"
    i = 0
    while size_bytes > 1024:
        i += 1
        size_bytes = size_bytes / 1024
    return f"{size_bytes:.2f}{sizes[i]}"

def get_list(dir_path):
    """
    returns a list containing all files in given directory dir_path
    each file in list contains  name, size, and access / modify time attribute of file
    return list will look like this
    [ (filename1, size, access_time), (filename2, size, acees_time) ]
    """
    dirs = []
    for fname in os.listdir(dir_path):
        path = os.path.join(dir_path, fname)
        if os.path.isfile(path):
            stats = os.stat(path)
            access_time = time.strftime("%H:%M %d-%b-%Y", time.gmtime(stats.st_mtime))
            size = get_size(stats.st_size)
            dirs.append([fname, size, access_time])
    return dirs
