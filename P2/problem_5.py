#!/usr/bin/env python
# coding: utf-8

# # Testing it all out
#
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# # Building a Trie in Python
#
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
#
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
#
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value):
        ## Initialize this node in the Trie
        self.value = value
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode(self.value + char)


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode("")

    def insert(self, word):
        ## Add a word to the Trie
        root = self.root
        len1 = len(word)

        for i in range(len1):
            char = word[i]
            if char not in root.children:
                root.insert(char)
            root = root.children[char]
            if i == len1 - 1:
                root.insert("$")

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        root = self.root
        len1 = len(prefix)

        for i in range(len1):
            char = prefix[i]
            if root.children == {}:
                return root
            if char not in root.children:
                return None
            root = root.children[char]

        return root


# # Finding Suffixes
#
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
#
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[2]:


class TrieNode:
    def __init__(self, value):
        ## Initialize this node in the Trie
        self.value = value
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode(self.value + char)

    def suffixes(self, suffix=""):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        if self.children == {}:
            return [self.value[len(suffix) : len(self.value) - 1]]
        arry = []
        for key, value in self.children.items():
            arry += value.suffixes(key)
        return arry


# In[3]:


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)


# In[4]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != "":
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print("\n".join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print("")


interact(f, prefix="")


# In[ ]:


# Test code below
# Test Case 1 - Normal case
print(MyTrie)  # <An object address>
print(MyTrie.find("trig").value)  # trig
print(MyTrie.find("trie").value)  # rie
t = MyTrie.find("f")
print(t.suffixes())  # ['un', 'unction', 'actory']

# Test Case 2 - Edge case - find a non-existing prefix
print(MyTrie.find("x"))  # None

# Test Case 3 - Edge case - find an empty string as prefix
print(MyTrie.find("").value)  # <empty string>

