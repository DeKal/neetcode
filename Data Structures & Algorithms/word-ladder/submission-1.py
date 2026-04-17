class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q = deque([(beginWord,1)])

        while q:
            top_word, cur_cnt = q.popleft()
            if top_word == endWord:
                return cur_cnt
            
            for c in range(len(top_word)):
                for ch in range(ord('a'), ord('z')+1):
                 
                    new_word = top_word[:c]+ chr(ch) + top_word[c+1:]

                    if new_word in word_set:
                        print(new_word)
                        q.append((new_word, cur_cnt+1))
                        word_set.remove(new_word) # remove word from set as already reach
                    
        return 0

