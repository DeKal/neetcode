

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur_root = self.root
        for ch in word:
            if ch not in cur_root:
                cur_root[ch] = {}
                
            cur_root = cur_root[ch]
        
        cur_root["$"] = word

    def remove(self, word):
        cur_root = self.root
        path = []
        for ch in word:
            # word not in trie -> exit
            if ch not in cur_root:
                return
            path.append((cur_root, ch))
            cur_root = cur_root[ch]
        
        if "$" not in cur_root:  # Word doesn't exist
            return

        del cur_root["$"]

        for parent, ch in reversed(path):
            if len(parent[ch]) == 0:
                del parent[ch]
            else:
                break
    
    
            


        

    
class Solution:

    
    def traverse(self, board, i , j, root, mark, results, trie):
        
        mark.add((i,j))
        new_root = root[board[i][j]]
    
        if "$" in new_root:
            results.add(new_root["$"])
            trie.remove(new_root["$"])


        z = [-1,1,0,0]
        k = [0,0,1,-1]
        n = len(board)
        m = len(board[0])
        
        for mv in range(0,4):
            new_i = i+z[mv]
            new_j = j+k[mv]
            if 0<=new_i<n and 0<=new_j<m:
                if board[new_i][new_j] in new_root and (new_i,new_j) not in mark:
                    self.traverse(board, new_i, new_j, new_root, mark, results, trie)
        mark.remove((i,j))



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
    

        n = len(board)
        m = len(board[0])

        results = set()
        mark = set()
    
        for i in range(0,n):
            for j in range(0, m):
                if board[i][j] in trie.root:
                    self.traverse(board, i, j, trie.root, mark, results, trie)

        return list(results)