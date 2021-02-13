The problem includes two phases: Coding and Encoding.
## A. Huffman Encoding
**Step 1**: Loop through each character of the data and build a dictionary to track the frequency: **time complexity** and **space complexity** are 0(n)  

**Step 2**: Remove two characters with the least frequency and reinsert the new value to build the Huffman tree until there is a single element left. 
Data structure choices:
1. An array takes O(n) to remove (go through the whole array to find item with the least frequency) and O(1) to insert if we keep track of empty indices, otherwise insertion will also take O(n)
2. A linked list takes O(n) to remove and 0(1) to insert at the head/ tail
3. A dictionary takes O(n) to remove and 0(1) to insert
4. A heap takes 0(log n) to remove and 0(log n) to insert. 
Therefore, we will implement a heap. A heap itself has space complexity of O(n) for each node is for each character. Besides, there will be 0(log n) calls on `_down_heapify()` to remove and 0(log n) calls on `_up_heapify()` to insert, so the functions's **space complexity** is 0(log n).

**Step 3**: Based on the Huffman tree, generate encoded data for our string message. 
- traverse the whole tree to reach all leaf nodes and create a unique binary code for each charater in a dictionary: **time complexity** is O(n log n) and **space complexity** is 0(n) 
- loop through each character of the data to return the encoded data: **time complexity** is O(n) and **space complexity** is 0(n log n) 

## B. Huffman Decoding
We traverse through the tree from the root using the encoded data and whenever we hit a leaf node, we get the character and go back to the root and continue the process until the end of the encoded data. Since the length of the encoded data is 0(n log n), **time complexity** is 0(n log n) and **space complexity** is 0(n).
