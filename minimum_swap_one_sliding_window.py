class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalones=sum(nums)
        n=len(nums)
        temp = [0] * (2 * n)
        for i in range(2*len(nums)):
            temp[i]=nums[i%n]
        i=0
        j=0
        currentOnes=0
        maxOnes=0

        while(j<2*n):
            if temp[j]==1:
                currentOnes+=1
            if(j-i+1>totalones):
                currentOnes-=temp[i]
                i+=1
            maxOnes=max(maxOnes,currentOnes)
            j+=1
        return totalones-maxOnes
            
