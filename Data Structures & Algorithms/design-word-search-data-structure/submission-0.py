class TrieNode:

    def __init__(self, isEndOfWord=False):
        self.children = {}
        self.isEndOfWord = isEndOfWord

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool: 
        options = [self.root]
        for c in word:
            if c == ".":
                new_options = []
                for _ in range(len(options)):
                    option = options.pop()
                    for child in option.children.values():
                        new_options.append(child)
                options = new_options
            else:
                new_options = []
                for _ in range(len(options)):
                    option = options.pop()
                    if c in option.children:
                        new_options.append(option.children[c])
                options = new_options

            if len(options) == 0:
                return False
            
        for option in options:
            if option.isEndOfWord:
                return True

        return False
