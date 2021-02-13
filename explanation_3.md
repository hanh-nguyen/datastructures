The problem includes two phases: Coding and Encoding.
## A. Huffman Encoding
**Step 1**: Loop through each character of the data and build a dictionary to track the frequency: 0(n)  

**Step 2**: Remove two characters with the least frequency and reinsert the new value to build the Huffman tree until there is a single element left. 
Data structure choices:
1. An array takes O(n) to remove (go through the whole array to find item with the least frequency) and O(1) to insert if we keep track of empty indices, otherwise insertion will also take O(n)
2. A linked list takes O(n) to remove and 0(1) to insert at the head/ tail
3. A dictionary takes O(n) to remove and 0(1) to insert
4. A heap takes 0(log n) to remove and 0(log n) to insert
Therefore, we will implement a heap.  

**Step 3**: Based on the Huffman tree, generate unique binary code for each character of our string message. We have to traverse the whole tree to reach all leaf nodes: O(n) and loop through each character of the data to return the encoded data: O(n)

## B. Huffman Decoding
We traverse through the tree from the root using the encoded data and whenever we hit a leaf node, we get the character and go back to the root and continue the process until the end of the encoded data: 0(n) (n is the length of the encoded data)
