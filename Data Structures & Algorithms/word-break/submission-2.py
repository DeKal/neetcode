# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s) + 1)
#         dp[0] = True

#         for i in range(len(s)):
#             if not dp[i]:
#                 continue
#             for w in wordDict:
#                 if s[i:i+len(w)] == w:
#                     dp[i + len(w)] = True

#         return dp[len(s)]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    # restart search every time from root
    def search(self, s: str, i: int, j: int) -> bool:
        node = self.root
        for k in range(i, j + 1):
            if s[k] not in node.children:
                return False
            node = node.children[s[k]]
        return node.isWord


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        maxLen = max(len(w) for w in wordDict)

        for i in range(n):
            if not dp[i]:
                continue

            for j in range(i, min(n, i + maxLen)):
                if trie.search(s, i, j):   # restart every time
                    dp[j + 1] = True

        return dp[n]
