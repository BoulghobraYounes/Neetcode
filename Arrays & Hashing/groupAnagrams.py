class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        results = []
        index = 0
        for s in range(len(strs)):
            if any(strs[s] in sublist for sublist in results):
                continue
            results.append([strs[s]])
            for t in range(s + 1, len(strs)):
                if self.isAnagram(strs[s], strs[t]):
                    results[index].append(strs[t])
            index += 1       
        return results 

    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countT == countS 


strs = ["", "", "act","pots","tops","cat","stop","hat"]
solution = Solution()
print(solution.groupAnagrams(strs))
print(solution.isAnagram("", ""))            


