class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False   
         
solution = Solution()
myList = [7, 8, 2, 6, 15]
myList2 = [19, 25, 26, 99, 25]
print(solution.hasDuplicate(myList))
print(solution.hasDuplicate(myList2))