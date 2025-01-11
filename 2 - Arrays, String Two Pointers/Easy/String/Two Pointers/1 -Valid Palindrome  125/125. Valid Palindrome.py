import re


def isPalindrome(s):
    # Step 1: Initialize two pointers
    left, right = 0, len(s) - 1

    # Step 2: Traverse the string from both ends
    while left < right:
        # Skip non-alphanumeric characters on the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters on the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters
        if s[left].lower() != s[right].lower():
            return False

        # Move both pointers inward
        left += 1
        right -= 1

    return True


# Example usage

print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(isPalindrome("race a car"))                     # Output: false
