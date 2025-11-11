class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # stores number -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


# Create an object of Solution
solution = Solution()

# Call the method correctly
print(solution.twoSum([1, 2, 3, 4], 7))
