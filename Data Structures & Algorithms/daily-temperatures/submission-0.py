class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        
        for idx, t1 in enumerate(temperatures):
            for i in range(idx+1, len(temperatures)):
                t2 = temperatures[i]
                if t2 > t1:
                    output[idx] = i - idx
                    break

        return output