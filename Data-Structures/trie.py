class Pointer:

    def __init__(self):
        self.a = [None for _ in range(30)]
        self.endPoint = False
        

class Trie:

    def __init__(self):
        self.head = Pointer()

    def insert(self, word: str) -> None:
        curr = self.head
        for v in word:
            nw = ord(v) - 97
            if curr.a[nw] is None:
                curr.a[nw] = Pointer()
            curr = curr.a[nw]
        curr.endPoint = True

    def search(self, word: str) -> bool:
        curr = self.head
        for v in word:
            nw = ord(v) - 97
            if curr.a[nw] is None:
                return False
            curr = curr.a[nw]
        return curr.endPoint

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for v in prefix:
            nw = ord(v) - 97
            if curr.a[nw] is None:
                return False
            curr = curr.a[nw]
        return True