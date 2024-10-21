class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)]) 
        visited = set([beginWord])
        while queue:
            currentWord, level = queue.popleft()
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = currentWord[:i] + c + currentWord[i+1:]
                    if newWord == endWord:
                        return level + 1
                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, level + 1))
        return 0



            