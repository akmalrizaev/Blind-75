## Valid Palindrome (LeetCode #125)

### Understanding the Question
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Inputs:
- `s`: A string (e.g., "A man, a plan, a canal: Panama").

Output:
- Boolean (`True` or `False`) indicating whether the string is a palindrome.

Constraints:
- \(1 \leq \text{len}(s) \leq 2 \times 10^5\)
- The string consists of printable ASCII characters.

---

## Brute Force Approach

### Explanation:
Filter out all non-alphanumeric characters from the string, convert it to lowercase, and check if the resulting string is equal to its reverse.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palindrome_brute_force(s):
    filtered_s = ''.join(char.lower() for char in s if char.isalnum())
    return filtered_s == filtered_s[::-1]
```

### Time Complexity:
`O(n)` where `n` is the length of the string, as we traverse the string twice.

### Space Complexity:
`O(n)` for the filtered string.

---

## Efficient Solution

### Explanation:
Use two pointers to check for palindrome properties without creating a new string. One pointer starts at the beginning of the string, and the other at the end. Skip non-alphanumeric characters and compare the characters at the two pointers.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### Time Complexity:
`O(n)` as we traverse the string once.

### Space Complexity:
`O(1)` since no extra space is used apart from pointers.

---

## Conclusion
The brute force approach creates a filtered string, which is simple but uses extra space. The efficient solution uses two pointers to achieve the same result in linear time with constant space, demonstrating the benefits of in-place techniques for string manipulation.
