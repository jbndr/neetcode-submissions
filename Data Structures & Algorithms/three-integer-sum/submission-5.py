class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()

        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums):
                for k,n3 in enumerate(nums):
                    indicies = set()
                    indicies.add(i)
                    indicies.add(j)
                    indicies.add(k)
                    if len(indicies) == 3:
                        if n1 + n2 + n3 == 0:
                            print(i,j,k,"----",n1,n2,n3)
                            sorted_list = sorted([n1,n2,n3])
                            n1_,n2_,n3_ = sorted_list
                            triplets.add((n1_,n2_,n3_))

        return list(triplets)

                        


        