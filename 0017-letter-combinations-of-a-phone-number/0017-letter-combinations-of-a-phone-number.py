class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
        if not digits:
            return []

        result = []
        def recursive(index, combination):
            if index == len(digits):
                result.append(combination)
                return

            letters = letter_map[digits[index]]
            for letter in letters:
                recursive(index+1, combination+letter)

        recursive(0, '')
        return result