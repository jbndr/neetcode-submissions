class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                for k, n3 in enumerate(nums):
                    if i < j < k and n1 + n2 + n3 == 0:
                        triplets.add(tuple(sorted((n1, n2, n3))))

        return list(triplets)

                        


        