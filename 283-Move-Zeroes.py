class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for current in range (len(nums)):
            if nums[current] != 0:
                nums[j] , nums[current] = nums[current], nums[j]
                j+=1
        