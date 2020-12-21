class TrieNode:
    def __init__(self, char):
        self.isWordEnd = False
        self.children = {}
        self.char = char
    def insert(self, char):
        self.children[char] = TrieNode(char)
    def suffixes(self, suffix=''):
        output = []
        def find(node, output_str):
            if node.isWordEnd:
                output.append(output_str)
            for char in node.children:
                #print(node.children[char].children, node.children[char].isWordEnd, node.children[char].char)
                tmp = output_str + char
                find(node.children[char], tmp)
        find(self, "")
        return output

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.isWordEnd = True
    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('a')