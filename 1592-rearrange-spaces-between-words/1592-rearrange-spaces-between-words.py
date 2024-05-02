class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')
        words = text.split()

        if len(words) == 1:
            return words[0] + ' ' * space_count

        return (' ' * (space_count // (len(words) - 1))).join(words) + ' ' * (space_count % (len(words) - 1))