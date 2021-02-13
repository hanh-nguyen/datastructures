import sys

def huffman_encoding(data):
    frequencies = {}
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    queue = Heap()
    for character, freq in frequencies.items():
        node = Node(value=freq, char=character)
        queue.insert(node)
    while queue.size() > 1:
        left = queue.remove()
        right = queue.remove()
        node = Node(value=left.value+right.value)
        node.left = left
        node.right = right
        queue.insert(node)

    huffman_codes = get_huffman_code(queue.get_root())
    encoded = [huffman_codes[char] for char in data]
    return ''.join(encoded), queue

def get_huffman_code(node):
    return _get_huffman_code(node, s="", d={})

def _get_huffman_code(node, s, d):
    if node is None:
        return
    if node.char:
        d[node.char] = s
    left_result = _get_huffman_code(node.left, s + "0", d)
    right_result = _get_huffman_code(node.right, s + "1", d)
    if left_result:
        d.update(left_result)
    if right_result:
        d.update(right_result)    
    return d


def huffman_decoding(data,tree):
    if tree.size() == 0: return ''
    node = tree.get_root()
    if data == '': return node.char * node.value
    result = ""
    for digit in data:
        if digit == '0':
            node = node.left
        elif digit == '1':
            node = node.right
        if node.char:
            result += node.char
            node = tree.get_root()
    return result

class Node:
    def __init__(self, value, char=None):
        self.value = value
        self.char = char
        self.left = None
        self.right = None
    
    def add_left_child(self, data):
        self.left = data

    def add_right_child(self, data):
        self.right = data

    def __str__(self):
        return (f"Char: {self.char}, Value: {self.value}, Left: {self.left}, Right: {self.right}")
class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0
    
    def get_root(self):
        return self.cbt[0]

    def size(self):
        return self.next_index

    def insert(self, node):
        self.cbt[self.next_index] = node
        self._up_heapify()
        self.next_index += 1
        if self.next_index >= len(self.cbt):
            self._double_size()

    def remove(self):
        if self.next_index == 0: return None

        top_node = self.cbt[0]
        self.next_index -= 1
        self.cbt[0] = self.cbt[self.next_index]
        self.cbt[self.next_index] = None
        self._down_heapify()
        return top_node
    
    def _down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            parent = self.cbt[parent_index]
            left_child = None
            right_child = None
            min_value = parent.value

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]
                
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]
                
            if left_child is not None:
                min_value = min(parent.value, left_child.value)
                
            if right_child is not None:
                min_value = min(right_child.value, min_value)
                
            if min_value == parent.value:
                return
            
            if min_value == left_child.value:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = left_child
                parent = left_child_index

            elif min_value == right_child.value:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = right_child
                parent = right_child_index

    def _up_heapify(self):
        child_index = self.next_index
        while child_index >=1:
            parent_index = (child_index - 1) // 2
            parent_node = self.cbt[parent_index]
            child_node = self.cbt[child_index]
            if parent_node.value > child_node.value:
                self.cbt[parent_index] = child_node
                self.cbt[child_index] = parent_node

                child_index = parent_index
            else:
                break

    def _double_size(self):
        old_cbt = self.cbt
        self.cbt = [None for _ in range(len(self.cbt) * 2)]
        for i in range(self.next_index):
            self.cbt[i] = old_cbt[i]

    def __repr__(self):
        s = ""
        for i in self.cbt:
            if i:
                s += str(i) + " -> "
        return s

def testing(example):
    print ("The size of the data is: {}\n".format(sys.getsizeof(example)))
    print ("The content of the data is: {}\n".format(example))

    encoded_data, tree = huffman_encoding(example)
    if encoded_data != '':
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    else:
        print ("The size of the encoded data is: 0\n")
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    example = "The bird is the word"
    testing(example)

    example = "This project is hard!"
    testing(example)

    example = "((ABCXYZ)"
    testing(example)

    example = "A"
    testing(example)

    example = "bbbbbb"
    testing(example)

    example = ""
    testing(example)