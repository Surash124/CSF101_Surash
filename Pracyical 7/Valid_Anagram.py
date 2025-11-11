# Create an instance of the Solution class
solution = Solution()

# Example inputs
s1, t1 = "listen", "silent"
s2, t2 = "hello", "world"

# Test and print results
print(f'Is "{s1}" an anagram of "{t1}"? {solution.isAnagram(s1, t1)}')
print(f'Is "{s2}" an anagram of "{t2}"? {solution.isAnagram(s2, t2)}')