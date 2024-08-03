class Solution:
    def generateParenthesis(self, n):
        
        def dfs(left, right, s):
            print(left, right, s)
            if len(s) == n * 2:
                res.append(s)
                print(res)
                return 

            if left < n:
                print("h",left, right, s)
                dfs(left + 1, right, s + '(')
                


            if right < left:
                print("R",left, right, s)
                dfs(left, right + 1, s + ')')
                

        res = []
        dfs(0, 0, '')
        return res
solution=Solution()
print(solution.generateParenthesis(3))