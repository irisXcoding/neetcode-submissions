from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        dq = deque([(beginWord, 1)])
        char = string.ascii_lowercase
        while dq:
            item, step = dq.popleft()
            for i in range(len(item)):
                for c in char:
                    new_word = item[:i]+c+item[i+1:]
                    if new_word == endWord:
                        return step+1
                    if new_word in words:
                        words.remove(new_word)
                        dq.append((new_word, step+1))
        return 0