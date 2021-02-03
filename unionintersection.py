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
    if llist_1.size() == 0: return llist_2
    if llist_2.size() == 0: return llist_1
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

"""Run time: 
Worst case complexity: O((a+b)**2)
Algorithm:
Let call the lengths of llist_1 and llist_2 are a & b
initialize an empty set: O(1)
loop through llist_1 and add each node value in the set: O(a*1) = O(a)
loop through llist_2 and add each node value in the set: O(b*1) = O(b)
initialize an empty linked list: O(1)
loop through the set, which is O(a+b) 
    and append each item to the linked list, appending requiring go through the entire linked list to the end: O(a+b),
    so the total run time is O((a+b)**2)
    if we design the append method to add item at the linked list head, the run time would be just O(a+b)
"""

def intersection(llist_1, llist_2):
    if llist_1.size() == 0: return None
    if llist_2.size() == 0: return None
    intersect = defaultdict(list)
    node_1 = llist_1.head
    while node_1:
        intersect[node_1.value] = [1]
        node_1 = node_1.next
    node_2 = llist_2.head
    while node_2:
        intersect[node_2.value].append(2)
        node_2 = node_2.next
    intersectll = LinkedList()
    for key, value in intersect.items():
        if value == [1, 2]:
            intersectll.append(key)
    return intersectll

"""Run time: 
Worst case complexity: O((a+b)**2)
Algorithm:
Let call the lengths of llist_1 and llist_2 are a & b
initialize an empty dictionary: O(1)
loop through llist_1 and add each node in the dictionary: O(a*1) = O(a)
loop through llist_2 and add each node in the dictionary: O(b*1) = O(b)
initialize an empty linked list: O(1)
loop through the dictionary, which is O(min(a,b)) 
    and append each item to the linked list, appending requiring go through the entire linked list to the end: O(min(a,b)),
    so the total run time is O(min(a,b)**2) 
    if we design the append method to add item at the linked list head, the run time would be just O(min(a,b)) 
"""

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))