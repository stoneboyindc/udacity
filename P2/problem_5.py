## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.value = None
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        # self.value = char


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = word[i]
            if index not in root.children:
                root.insert(index)  # [index].insert(index)
            root = root.children[index]

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        root = self.root
        len1 = len(prefix)

        for i in range(len1):
            index = prefix[i]
            if index not in root.children:
                break
            root = root.children[index]

        return root


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.value = None
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.value = char
        self.children[char] = TrieNode()

    def suffixes(self, suffix=""):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        for c in self.children:
            c.value + c.suffix()
        return c.value + c.suffix()


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

print(MyTrie)

# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact


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

