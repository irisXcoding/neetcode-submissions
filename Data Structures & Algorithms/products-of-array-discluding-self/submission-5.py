class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        res = [1]*n
        right = 1
        for i in range(n):
            res[i] =  res[i-1]*nums[i]
        for idx in range(n-1, -1, -1):
            if idx==0:
                res[idx] = right
            else:
                res[idx] = res[idx-1]*right
            right*=nums[idx]
        return res