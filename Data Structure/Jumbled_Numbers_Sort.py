class Solution(object):
    def sortJumbled(self, mapping, nums):
       def mapper(num):
        mapped_str=''
        for c in str(num):
            mapped_str+=str(mapping[int(c)])
        print(mapped_str)
        return int(mapped_str)
       
       nums.sort(key=mapper)
       return nums

solution=Solution()
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [30,338,38]
print(solution.sortJumbled(mapping,nums))      