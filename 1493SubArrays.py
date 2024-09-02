class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev=0
        curr=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr+=1
            else:
                ans=max(ans,prev+curr)
                prev=curr
                curr=0
            ans=max(ans,prev+curr)
        return ans-1 if ans==len(nums) else ans
