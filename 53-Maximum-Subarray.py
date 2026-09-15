class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        mx=float ("-inf")
        sum=0

        for i in range(len(nums)):
            sum= sum +nums[i]
            mx=max(sum,mx)
            if (sum<0):
                sum=0
            
            
        return mx