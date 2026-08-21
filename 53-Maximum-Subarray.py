class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sum = nums[0]
        bestsum =nums[0]
        for x in nums[1::]:
            sum =max(x,sum+x)
            bestsum=max(sum,bestsum)
        return bestsum