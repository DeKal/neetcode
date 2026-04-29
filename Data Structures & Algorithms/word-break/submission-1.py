class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

def buildTrie(wordDict):
    root = TrieNode()
    for w in wordDict:
        node = root
        for c in w:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
    return root


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = buildTrie(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]

                if node.isWord:
                    dp[j + 1] = True

        return dp[n]