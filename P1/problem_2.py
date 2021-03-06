import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []
    try:
        listDirs = os.listdir(path)
        for i in listDirs:
            item = os.path.join(path, i)
            if os.path.isdir(item):
                result += find_files(suffix, item)
            if os.path.isfile(item):
                if item.endswith(suffix):
                    result.append(item)
    except FileNotFoundError:
        print (path, "does not exist.")
    except NotADirectoryError:
        if path.endswith(suffix):
            result.append(path)
    return result

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

# Test code below
# Test Case 1 - Normal case - Use provided `testdir.zip` file

print (find_files(".c", "C:\\Temp\\testdir\\testdir"))  # ['C:\\Temp\\testdir\\testdir\\subdir1\\a.c', 'C:\\Temp\\testdir\\testdir\\subdir3\\subsubdir1\\b.c', 'C:\\Temp\\testdir\\testdir\\subdir5\\a.c', 'C:\\Temp\\testdir\\testdir\\t1.c']

# Test Case 2 - Edge case - Use a file as an input argument for path
print (find_files(".c", "C:\\Temp\\testdir\\testdir\\subdir1\\a.c"))  # ['C:\\Temp\\testdir\\testdir\\subdir1\\a.c']

# Test Case 3 - Edge case - Use provided `testdir.zip` file but the wrong input
print (find_files(".cpp", "C:\\Temp\\testdir\\testdirX"))  # [] with an error message printed out C:\\Temp\\testdir\\testdirX does not exist.
