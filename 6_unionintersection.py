from collections import defaultdict
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    union_set = set()
    node_1 = llist_1.head
    while node_1:
        union_set.add(node_1.value)
        node_1 = node_1.next
    node_2 = llist_2.head
    while node_2:
        union_set.add(node_2.value)
        node_2 = node_2.next
    unionll = LinkedList()
    for item in union_set:
        unionll.append(item)
    return unionll


def intersection(llist_1, llist_2):
    intersect = defaultdict(list)
    node_1 = llist_1.head
    while node_1:
        intersect[node_1.value] = [1]
        node_1 = node_1.next
    node_2 = llist_2.head
    while node_2:
        if 2 not in intersect[node_2.value]:
            intersect[node_2.value].append(2)
        node_2 = node_2.next
    intersectll = LinkedList()
    for key, value in intersect.items():
        if value == [1, 2]:
            intersectll.append(key)
    return intersectll

# Test 1
print("Test 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2))
# 4 -> 6 -> 21 ->

# Test 2
print("Test 2")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print (intersection(linked_list_1,linked_list_2))
# Nothing printed because they do not overlap

# Test 3
print("Test 3")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

print (union(linked_list_1,linked_list_2))
# 1 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2))
# Nothing printed because they do not overlap

# Test 4
print("Test 4")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

print (union(linked_list_1,linked_list_2))
# Nothing printed because both are empty linked lists
print (intersection(linked_list_1,linked_list_2))
# Nothing printed because they do not overlap

# Test 5
print("Test 5")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1]
element_2 = [1,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 1 -> 
print (intersection(linked_list_1,linked_list_2))
# 1 -> 
