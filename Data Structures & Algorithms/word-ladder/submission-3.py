class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q = deque([(beginWord,1)])

        pattern_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        while q:
            top_word, cur_cnt = q.popleft()
            if top_word == endWord:
                return cur_cnt
            
            for c in range(len(top_word)):
              
                new_pattern = top_word[:c]+ "*" + top_word[c+1:]
                for new_word in pattern_map[new_pattern]:
                    if new_word in word_set:
                        q.append((new_word, cur_cnt+1))
                        word_set.remove(new_word) # remove word from set as already reach
                
                pattern_map[new_pattern] = []
                    
        return 0

