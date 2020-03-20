# Data Structure
It is a tree structure where each node contains a value, a handler, and a dictonary object that holds the children nodes.

# Time Complexity
Given 'n' as the number of a URI segments, the insert() operation is O(n) as it needs to iterate through each uri segment and add
the segment into a node in the tree.
Given 'n' as the largest number of URI segments for a URI, the find() operation is O(n) as it needs to traverse all the ways to the leaf node to find the handler.

# Space Complexity
Given 'n' as the number of a URI segments, and 'm' as the longest length of an URI segment, it needs to hold all the URI 
segments in a tree. Therefore, it is O(n*m)