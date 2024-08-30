class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        maxCandit=max(candies)
        for i in range(len(candies)):
            if extraCandies+candies[i]>=maxCandit:
                output.append(True)  
            else:
                output.append(False)
        return output
