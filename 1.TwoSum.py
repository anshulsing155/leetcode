class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = []
        for i , a in enumerate(nums):
            for j , b in enumerate(nums):
                if a+b == target and i!=j:
                    c.append(i)
                    c.append(j)
                    return c
                    braek