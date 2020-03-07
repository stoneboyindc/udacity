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

# Implementation
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        for i in group.get_groups():
            return is_user_in_group(user, i)
    return None


# sample data
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test code below
# Test Case 1 - Normal case
print(is_user_in_group(sub_child_user, parent))  #True

# Test Case 2 - Normal case
not_found_user = "not_found"
print(is_user_in_group(not_found_user, parent))  #None

# Test Case 3 - Edge case - empty string input
empty_string = ""
print(is_user_in_group(empty_string, parent))  #None

# Test Case 4 - Edge case - Null input
print(is_user_in_group(None, parent))  #None
