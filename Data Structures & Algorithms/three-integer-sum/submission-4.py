class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        n = len(nums)
        for idx, fix_num in enumerate(sorted_nums):
            if idx>0 and fix_num == sorted_nums[idx-1]:
                continue
            target = -fix_num
            left, right = idx+1, n-1
            while left<right:
                if sorted_nums[left]+sorted_nums[right] == target:
                    res.append([fix_num, sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1
                    while left< n and sorted_nums[left] == sorted_nums[left-1]:
                        left+=1
                    while right >=0 and sorted_nums[right] == sorted_nums[right + 1]:
                        right-= 1
                elif sorted_nums[left]+sorted_nums[right] < target:
                    left += 1
                else:
                    right-=1
        return res