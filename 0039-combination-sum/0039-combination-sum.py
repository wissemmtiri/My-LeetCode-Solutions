class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursive(candidates, target, path, res):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                recursive(candidates[i:], target -
                          candidates[i], path + [candidates[i]], res)
        res = []
        recursive(candidates, target, [], res)
        return res