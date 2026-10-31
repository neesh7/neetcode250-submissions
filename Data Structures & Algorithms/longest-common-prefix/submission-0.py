class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ls = strs
        if not ls: # empty list -> no prefix
            return ""
        final_str = ""
        size = len(ls[0]) # prefix can't be longer than the first string
        for i in range(size): # 0, 1, 2
            ch = ls[0][0:i+1] # candidate prefix of length i+1
            for j in range(1, len(ls)): # compare with every other string
                comp_str = ls[j][0:i+1]
                if ch != comp_str: # mismatch (or ls[j] too short)
                    return final_str
            final_str = ch # ch matched ALL strings
        return final_str