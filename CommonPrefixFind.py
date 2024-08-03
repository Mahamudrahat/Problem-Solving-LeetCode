class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort()
        result = ""
        s1 = strs[0]
        s2 = strs[-1]
        
        for i in range(len(s1)):
            if i < len(s2) and s1[i] == s2[i]:
                result += s1[i]
            else:
                break
        
        return result

# Example usage:
solution = Solution()
strs = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs))  # Output: "fl"
