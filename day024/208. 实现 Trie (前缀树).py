class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()

    def insert(self, word: str) -> None:
        # 时间复杂度O(N)，空间复杂度O(N)，N为word的长度
        """
        Inserts a word into the trie.
        """
        temp = self.dic
        for s in word:
            if s in temp:
                temp = temp[s]
            else:
                temp[s] = dict()
                temp = temp[s]
        temp['end'] = True

    def search(self, word: str) -> bool:
        # 时间复杂度O(N)，空间复杂度O(1)，N为word的长度
        """
        Returns if the word is in the trie.
        """
        temp = self.dic
        for s in word:
            if s in temp:
                temp = temp[s]
            else:
                return False
        return 'end' in temp

    def startsWith(self, prefix: str) -> bool:
        # 时间复杂度O(N)，空间复杂度O(1)，N为prefix的长度
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.dic
        for s in prefix:
            if s in temp:
                temp = temp[s]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
