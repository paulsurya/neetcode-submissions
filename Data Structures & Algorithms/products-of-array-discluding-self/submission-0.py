class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix_prod
            prefix_prod *= nums[i]
        
        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return res