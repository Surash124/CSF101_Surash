class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            a = target - num
            if a in num_map:
                return [num_map[a],i]
            num_map[num]=i
        return []
# Create an instance of the Solution class
solution = Solution()

# Example input
nums = [2, 7, 11, 15]
target = 9

# Test and print the result
result = solution.twoSum(nums, target)
print(f"Indices of numbers that add up to {target}: {result}")