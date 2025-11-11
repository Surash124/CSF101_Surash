class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
# Create an instance of the Solution class
solution = Solution()

# Example input lists
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 2, 5]

# Test and print the results
print(f"Does nums1 contain duplicates? {solution.containsDuplicate(nums1)}")
print(f"Does nums2 contain duplicates? {solution.containsDuplicate(nums2)}")