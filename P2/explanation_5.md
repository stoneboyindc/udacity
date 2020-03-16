# Data Structure
It is a tree structure where each node contains a value and a dictonary object that holds the children nodes.

# Time Complexity
Given 'n' as the length of a word, the insert() operation is O(n) as it needs to iterate through the word and add
a character into a node in the tree.
Given 'n' as the total number of words and 'm' as the longest length of the word, the suffix() operation is O(n*m) as 
in the worst case, it needs to traverse all the nodes in the tree.

# Space Complexity
Given 'n' as the total number of words and 'm' as the longest length of the word, it needs to hold all the words in a
tree. Therefore, it is O(n*m)