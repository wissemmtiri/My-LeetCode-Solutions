class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for string in strs:
            id = "".join(sorted(string))
            if id in mapper:
                mapper[id].append(string)
            else:
                mapper[id] = [string]
        return list(mapper.values())