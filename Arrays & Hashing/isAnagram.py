class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countT == countS 

        """
        sc1 = sorted(s)
        sorted_s = "".join(sc1)
        sc2 = sorted(t)
        sorted_t = "".join(sc2)
        if sorted_s == sorted_t:
            return True
        else:
            return False
        """
            
solution = Solution()
print(solution.isAnagram("racecar","carrace"))
print(solution.isAnagram("jar","jam"))