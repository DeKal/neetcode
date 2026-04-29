class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        n = len(words)
        edges = defaultdict(set)
        in_degrees = defaultdict(int)
        char_set = set([c for w in words for c in w])

        for i in range(n-1):
            word = words[i]
            nxt_word = words[i+1]
            min_length = min(len(word), len(nxt_word))

            # if given abc and abcdef -> this is invalid order
            if len(word) > len(nxt_word) and word[:min_length] == nxt_word[:min_length]:
                return ""

            for j in range(min_length):
                if word[j] != nxt_word[j]:
                    if nxt_word[j] not in edges[word[j]]:
                        edges[word[j]].add(nxt_word[j])
                        in_degrees[nxt_word[j]] += 1

                    char_set.add(word[j])
                    char_set.add(nxt_word[j])

                    # break as we have found the difference 
                    break

        # print(edges)
        # print(in_degrees)
        # print(char_set)

        q = deque([])
        for ch in char_set:
            if ch not in in_degrees:
                q.append(ch)
        res = []

        while q:
            top = q.popleft()
            res.append(top)
            vertices = edges[top]
            
            for v in vertices:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    q.append(v)
    
        if len(res) != len(char_set):
            return ""

        return "".join(res)

