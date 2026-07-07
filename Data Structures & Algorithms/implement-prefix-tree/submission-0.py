class TreeNode:

    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end
    

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            is_end = i == len(word) - 1
            char = word[i]

            if char not in node.children:
                node.children[char] = TreeNode(is_end)
            else:
                if is_end:
                    node.children[char].is_end = True

            node = node.children[char]

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
        
        