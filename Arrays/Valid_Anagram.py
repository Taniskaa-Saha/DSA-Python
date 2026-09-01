class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            return sorted(s)==sorted(t)
        return False

solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))