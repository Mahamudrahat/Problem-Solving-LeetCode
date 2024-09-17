import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1=len(str1)
        n2=len(str2)
        if(str1+str2!=str2+str1):
            return ""
        return str1[:gcd(n1,n2)]