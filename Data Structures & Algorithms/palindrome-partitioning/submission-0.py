class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solutions = []
        n = len(s)

        def bt(path, start):
            if start == n:
                solutions.append(path.copy())
                return

            for end in range(start+1, n+1):
                substr = s[start:end]
                if substr != substr[::-1]:
                    continue
                
                path.append(substr)
                bt(path, end)
                path.pop()

        bt([], 0)

        return solutions
        