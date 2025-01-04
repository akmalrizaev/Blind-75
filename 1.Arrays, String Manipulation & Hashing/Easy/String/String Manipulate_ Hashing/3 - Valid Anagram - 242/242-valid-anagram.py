# ---------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        # Convert both to lowercase to ignore case match
        str1 = str1.lower()
        str2 = str2.lower()

        # Strip off all the white spaces
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")

        # Initialize the bucket array
        counts = [0] * 26

        # Fill the buckets
        for char in str1:
            counts[ord(char) - ord('a')] += 1

        # Empty the buckets
        for char in str2:
            counts[ord(char) - ord('a')] -= 1

        # Check if all buckets are empty
        for count in counts:
            if count != 0:
                return False

        return True

# ---------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(n)


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    return count_s == count_t


# Example usage
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))  # Output: False
