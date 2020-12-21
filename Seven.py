class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler
    def insert(self, path, handler):
        self.children[path] = RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
       self.root = RouteTrieNode(handler)
    def insert(self, path, handler):
        current_node = self.root
        for sub in path:
            if sub not in current_node.children:
                current_node.children[sub] = RouteTrieNode()
            current_node = current_node.children[sub]
        current_node.handler = handler
    def find(self, path):
        current_node = self.root
        if path == ['/']:
            return current_node.handler
        for sub in path:
            if sub not in current_node.children:
                return None
            current_node = current_node.children[sub]
            #print(current_node.handler)
        return current_node.handler

class Router(RouteTrie):
    def __init__(self, rootHandle):
        # Create a new RouteTrie for holding our routes
        RouteTrie.__init__(self, rootHandle)
    def add_handler(self, paths, handler):
        path_list = self.split_path(paths)
        self.insert(path_list, handler)
    def split_path(self, paths):
        split = paths.split('/')
        split.remove('')
        if split == ['']:
            return ['/']
        return split
    def lookup(self, lookup):
        split = self.split_path(lookup)
        found = self.find(split)
        if found == None:
            return "No handler found"
        else:
            return found
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

# create the router and add a route
router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))
print(router.lookup("/home"))
print(router.lookup("/home/about"))
"""
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))
"""