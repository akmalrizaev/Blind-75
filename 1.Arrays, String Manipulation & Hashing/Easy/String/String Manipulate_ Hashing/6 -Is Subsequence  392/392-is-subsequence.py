# Approach: Two-Pointer Technique
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer in s if characters match
            j += 1  # Always move pointer in t

        return i == len(s)  # Check if all characters in s were matched


# Example usage
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: true
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: false
