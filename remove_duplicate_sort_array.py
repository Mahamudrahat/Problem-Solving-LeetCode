class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for num in nums:
        	if i<1 or num>nums[i-1]:
        		nums[i]=num
        		i+=1
        return (i,nums[0:i])
list=[0,0,1,1,1,2,2,3,3,4]
solution=Solution()
print(solution.removeDuplicates(list))