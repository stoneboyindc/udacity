# Data Structure
Active Directory is a tree like structure where a group can contain a subgroup and or users. Users are leaf nodes in this tree structure.

# Time Complexity
Each group and user is visited once by this recursive function. Given 'n' as the total number of groups and users, 
the time complexity is O(n)

# Space Complexity
In this recursive function to look for a group, only one variable is needed to keep track whether a user is found in the group.
Therefore, the space complexity is O(1)