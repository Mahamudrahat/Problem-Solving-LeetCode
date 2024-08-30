class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        sum=0
        n=len(nums)
        max_avg=float('-inf')
        avg=0
        for r in range(n):
            sum+=nums[r]
            if (r-l+1==k):
                max_avg=max(max_avg,sum/k)
                sum-=nums[l]
                l+=1
            
        return max_av