class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        suffix=1
        ans=[1]*n
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffix *= nums[i+1]
            ans[i] *= suffix

        return ans        