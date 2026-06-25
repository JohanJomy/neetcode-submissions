class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # patterns are matched with words
        # eg : *ag = [bag, sag, dag]
        adjmap = defaultdict(list)

        for word in wordList:

            # create patter for each letter, *og, d*g, do*
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adjmap[pattern].append(word)
        # print(adjmap)
        visited = set()
        # visited.add(beginWord)

        q = deque()
        q.append(beginWord)

        level = 1

        while q:
            # print(q)
            for _ in range(len(q)):
                word = q.popleft()
                visited.add(word)
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for j in adjmap[pattern]:
                        if j == endWord:
                            return level + 1
                        if j not in visited:
                            q.append(j)
                        

            level += 1
        return 0