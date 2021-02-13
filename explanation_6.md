## Union function
Run time: 
Worst case **time complexity**: O($(a+b)^2$)  

Algorithm:
Let call the lengths of llist_1 and llist_2 are a & b
- initialize an empty set: O(1)
- loop through llist_1 and add each node value in the set: O(a*1) = O(a)
- loop through llist_2 and add each node value in the set: O(b*1) = O(b)
- initialize an empty linked list: O(1)
- loop through the set, which is O(a+b) and append each item to the linked list, appending requiring go through the entire linked list to the end: O(a+b), so the total run time is O($(a+b)^2$). If we design the append method to add item at the linked list head, the run time would be just O(a+b)  

**Space complexity** is O(a + b)

## Intersect function
Run time: 
Worst case **time complexity**: O($(min(a,b))^2$)  

Algorithm:
Let call the lengths of llist_1 and llist_2 are a & b
- initialize an empty dictionary: O(1)
- loop through llist_1 and add each node in the dictionary: O(a*1) = O(a)
- loop through llist_2 and add each node in the dictionary: O(b*1) = O(b)
- initialize an empty linked list: O(1)
- loop through the dictionary, which is O(min(a,b)) and append each item to the linked list, appending requiring go through the entire linked list to the end: O(min(a,b)), so the total run time is O($(min(a,b))^2$). If we design the append method to add item at the linked list head, the run time would be just O(min(a,b))

**Space complexity** is O(a + b)