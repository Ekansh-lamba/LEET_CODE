class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2=[]
        for i in range(len(nums)):
            if (nums[i] in nums2):
                continue
            else:
                nums2.append(nums[i])
        k=len(nums2)
        nums[:k]=nums2
        return k