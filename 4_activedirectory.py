class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not isinstance(group, Group):
        print (f"{group} is not the group")
        return
    if user in group.users:
        return True
    for sub_group in group.groups:
        found = is_user_in_group(user, sub_group)
        if found: return True
    return False

# test
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, child)) # True
print(is_user_in_group(sub_child_user, parent)) # True
print(is_user_in_group(parent, child)) # False
print(is_user_in_group(parent, sub_child)) # False

not_child = "not_a_child"
print(is_user_in_group(not_child, parent)) # False
print(is_user_in_group(parent, sub_child_user)) # sub_child_user is not the group None

