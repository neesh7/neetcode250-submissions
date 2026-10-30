class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1, string2 = s, t
        # Basic check
        if len(string1) == len(string2):
            data1 = Solution().count_occurances(string1)
            data2 = Solution().count_occurances(string2)
            if data1 == data2:
                return True
        return False


    def count_occurances(self, str1: str) -> dict:
        data = {}
        for ch in str1:
            data[ch] = data.get(ch, 0) + 1
        print(data)
        return data