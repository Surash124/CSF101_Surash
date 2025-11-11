class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

# Create an instance of Solution
solution = Solution()

# Example inputs
test1 = "A man, a plan, a canal: Panama"
test2 = "race a car"

# Test and print results
print(f'Is "{test1}" a palindrome? {solution.isPalindrome(test1)}')
print(f'Is "{test2}" a palindrome? {solution.isPalindrome(test2)}')
