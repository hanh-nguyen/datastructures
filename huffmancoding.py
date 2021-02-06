import sys

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

class Node:
    def __init__(self, value, character=None):
        self.value = value
        self.char = charater

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def insert(self, node):
        self.cbt[self.next_index] = node
        self._up_heapify()
        self.next_index += 1
        if self.next_index >= len(self.cbt):
            self._double_size()

    def remove(self, node):
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

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            if left_child is not None:
                min_value = min(parent.value, left_child.value)

            if right_child is not None:
                min_element = min(right_child.value, min_element)

            if min_value == parent.value:
                return
            
            if min_value == left_child.value:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_value
                parent = left_child_index

            elif min_value == right_child.value:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_value
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



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))