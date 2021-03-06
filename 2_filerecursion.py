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
    if not os.path.exists(path):
        print("Path does not exist")
        return []

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    if os.path.isdir(path):
        results = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            result = find_files(suffix, item_path)
            if result:
                results += result
        return results

# Test
print(find_files('.c', 'testdir')) # ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
print(find_files('.h', 'testdir')) # ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']
print(find_files('.c', '')) # Path does not exist []
print(find_files('.c', 'testdir/subdir3')) # ['testdir/subdir3/subsubdir1/b.c']
print(find_files('.c', 'testdir/subdir9')) # Path does not exist []
print(find_files('.m', 'testdir')) # []