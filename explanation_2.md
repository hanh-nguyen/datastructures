The goal is to write code for finding all files under a directory (and all directories beneath it) that end with a suffix. If we find any file that meet the criteria, we add it into the result. An array is a good data structure to store the result because adding will take 0(1).

Since we will search all the files in the directory to check and if we see a sub-directory, we will search all the files in that sub-directory as well. The pattern repeats so we can use `recursion`. 

The **time complexity** and **space complexity** will be O(n), for n is the total number of files in the main directory and sub-directories.