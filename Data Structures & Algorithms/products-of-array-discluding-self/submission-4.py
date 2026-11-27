class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prefix_list = [1]*n
        surfix_list = [1]*n
        res = [0]*n
        for i in range(1, n):
            prefix_list[i] =  prefix_list[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            surfix_list[i] =surfix_list[i+1]*nums[i+1]
        for idx in range(n):
            res[idx] = prefix_list[idx]*surfix_list[idx]
        return res