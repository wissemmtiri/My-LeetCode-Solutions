class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)
        if "0000" in deadend:
            return -1
        if target == "0000":
            return 0
        queue = [("0000", 0)]
        while queue:
            current, steps = queue.pop(0)
            for i in range(4):
                for move in [-1, 1]:
                    new = current[:i] + \
                        str((int(current[i]) + move) % 10) + current[i + 1:]
                    if new == target:
                        return steps + 1
                    if new not in deadend:
                        deadend.add(new)
                        queue.append((new, steps + 1))

        return -1