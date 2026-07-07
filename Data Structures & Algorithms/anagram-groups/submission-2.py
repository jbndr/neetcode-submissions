class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for value in strs:
            sorted_value = ''.join(sorted(value))
            if sorted_value in groups:
                groups[sorted_value].append(value)
            else:
                groups[sorted_value] = [value]

        return [groups[key] for key in groups]