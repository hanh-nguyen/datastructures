We check if a user is in the list `users` of the group, and if the group has any sub-group, we check if a user is in the list `users` of the sub-group as well. The pattern repeats so we can use `recursion`. The runtime will be O(a + b * c), for a is # users, b is # sub-groups and c is # users of sub-groups.