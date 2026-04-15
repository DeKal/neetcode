class PrefixTree:

    def __init__(self):
        self.wd = {}


    def insert(self, word: str) -> None:
        cur_dict = self.wd
        for c in word:
            if c not in cur_dict:
                cur_dict[c] = {}
            cur_dict = cur_dict[c]
        cur_dict["$"] = {}

    def search(self, word: str) -> bool:
        cur_dict = self.wd
        for c in word:
            if c not in cur_dict:
                return False
            cur_dict = cur_dict[c]
        
        return True if "$" in cur_dict else False

    def startsWith(self, prefix: str) -> bool:
        cur_dict = self.wd
        for c in prefix:
            if c not in cur_dict:
                return False
            cur_dict = cur_dict[c]

        return True
        