class WordDictionary:

    def __init__(self):
        self.wd = {}

    def addWord(self, word: str) -> None:
        cur_dict = self.wd
        for c in word:
            if c not in cur_dict:
                cur_dict[c] = {}
            cur_dict = cur_dict[c]
        cur_dict["$"] = {}

    def search(self, word: str) -> bool:

        def dfs(root, j):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for key, node in cur.items():
                        if dfs(node, i+1):
                            return True
                    return False

                else:
                    if c not in cur:
                        return False
                    cur = cur[c]

            return True if "$" in cur else False
        
        return dfs(self.wd, 0)



        
