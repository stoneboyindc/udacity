# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value, handler):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.handler = handler
        self.children = {}

    def insert(self, segment, handler):
        # Insert the node as before
        self.children[segment] = RouteTrieNode(segment, handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode("ROOT", handler)

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        root = self.root
        len1 = len(paths)

        for i in range(len1):
            char = paths[i]
            if char not in root.children:
                if i == len1 - 1:
                    root.insert(char, handler)
                else:
                    root.insert(char, None)
            root = root.children[char]

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        root = self.root
        handler = self.root.handler
        len1 = len(paths)
        if len1 == 0:
            return self.root.handler
        for i in range(len1):
            char = paths[i]
            # if root.children == {}:
            #     return handler
            if char not in root.children:
                return None
            # if char in root.children and root.children[char].children == {}:
            #     return root.children[char].handler
            root = root.children[char]
            handler = root.handler
            if i == len1 - 1 and char == root.value:
                return handler

        return None


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, rootHandler, notFoundHandler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(rootHandler)
        self.notFoundHandler = notFoundHandler

    def add_handler(self, uri, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routeTrie.insert(self.split_path(uri), handler)

    def lookup(self, uri):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        # paths = self.split_path(uri)
        h = self.routeTrie.find(self.split_path(uri))
        if h == None:
            return self.notFoundHandler
        else:
            return h

    def split_path(self, uri):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        segments = uri.split("/")
        # print("segments: ", segments)
        paths = []
        for i in segments:
            if i != "":
                paths.append(i)
        # print("paths: ", paths)
        return paths


# Test code below
# Test Case 1 - Normal case

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(
    router.lookup("/home")
)  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(
    router.lookup("/home/about/")
)  # should print 'about handler' or None if you did not handle trailing slashes
print(
    router.lookup("/home/about/me")
)  # should print 'not found handler' or None if you did not implement one

# Test Case 2 - Edge case - empty path
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

print(router.lookup(""))  # should print 'root handler'

# Test Case 3 - Edge case - an invalid path
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

print(router.lookup("home"))  # should print "not found handler"
