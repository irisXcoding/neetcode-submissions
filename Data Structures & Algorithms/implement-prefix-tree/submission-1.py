class TrieNode:
    def __init__(self, is_end=False):
        self.child = {}
        self.is_end = is_end


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        n = len(word)
        for idx, c in enumerate(word):
            if c not in cur.child:
                if idx == n - 1:
                    cur.child.update({c: TrieNode(True)})
                else:
                    cur.child.update({c: TrieNode()})
            elif idx==n-1:
                cur.child[c].is_end = True
            cur = cur.child[c]

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            cur = cur.child.get(c)
            if not cur:
                return False
        if cur.is_end==False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            cur = cur.child.get(c)
            if not cur:
                return False
        return True
