class Solution:
    def compress(self, chars: List[str]) -> int:
        lengthChars=len(chars)
        if lengthChars< 2:
            return lengthChars
        index=0
        i=0

        while(i<lengthChars):
            
            count=1
            while(i<lengthChars-1 and chars[i]==chars[i+1]):
                count+=1
                i+=1
            chars[index]=chars[i]
            index+=1

            if(count>1):
                for val in str(count):
                    chars[index]=val
                    index+=1
            i+=1
        return index