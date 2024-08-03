class Solution(object):
    def isValid(self, s:str)->bool:
        stack=[]
        parenDictionary={')':'(','}':'{',']':'['}

        for c in s:
            print(c)
            if c in parenDictionary:
                if stack and stack[-1]==parenDictionary[c]:
                    print(stack)
                    stack.pop()
                else:
                    return False
            else:
                print(stack)
                stack.append(c)
        return True if not stack else False
solution = Solution()
s = "(((((()))"
print(solution.isValid(s))
        