class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            print(f"iteration {i}: {prevMap}")
            
solution = Solution()
nums = [2, 5, 1, 6]
target = 8
print(solution.twoSum(nums, target))