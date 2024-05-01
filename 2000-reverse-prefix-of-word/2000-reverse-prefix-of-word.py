class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        while index < len(word) and word[index] != ch:
            index += 1
        if index == len(word):
            return word
        for i in range(index//2 + 1):
            word = list(word)
            word[i], word[index-i] = word[index-i], word[i]
            word = ''.join(word)
        return word