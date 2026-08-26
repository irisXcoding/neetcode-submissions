class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] <nums[right] or left == right:
                return nums[left]
            else:
                mid = int((left+right)/2)
                if nums[mid]>=nums[left]:
                    left = mid+1
                else:
                    right = mid
                # if nums[mid]<nums[right]:
                #     right = mid
                # else:
                #     left = mid+1
