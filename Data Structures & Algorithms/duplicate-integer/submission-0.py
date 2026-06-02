class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = list()

        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            else:
                freq.append(nums[i])
        return False