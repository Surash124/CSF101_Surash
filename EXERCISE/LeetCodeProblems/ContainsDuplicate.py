class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Create an object of the class
solution = Solution()

# Call the method and print the result
print(solution.containsDuplicate([1, 2, 3, 1]))  # Expected output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Expected output: False
