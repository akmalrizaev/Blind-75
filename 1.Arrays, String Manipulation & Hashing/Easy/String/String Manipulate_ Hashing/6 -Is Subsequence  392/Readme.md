## Is Subsequence (LeetCode #392)

### Understanding the Question
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise. A subsequence is a sequence that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Inputs:
- `s`: A string (e.g., "abc").
- `t`: A string (e.g., "ahbgdc").

Output:
- Boolean (`True` or `False`).

Constraints:
- \(0 \leq \text{len}(s) \leq 100\)
- \(0 \leq \text{len}(t) \leq 10^4\)
- `s` and `t` consist of lowercase English letters.

---

## Brute Force Approach

### Explanation:
Iterate through the string `t` and check if the characters of `s` appear in the same order by using a pointer to traverse `s`. If all characters in `s` are found in sequence, return `true`. Otherwise, return `false`.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_subsequence_brute_force(s, t):
    if not s:
        return True
    s_pointer = 0
    for char in t:
        if char == s[s_pointer]:
            s_pointer += 1
        if s_pointer == len(s):
            return True
    return False
```

### Time Complexity:
`O(n)` where `n` is the length of `t`.

### Space Complexity:
`O(1)` as no extra space is used apart from pointers.

---

## Efficient Solution

### Explanation:
This approach is already efficient, as the brute force solution achieves the optimal time complexity. For large-scale applications, if multiple `s` strings need to be checked against the same `t`, preprocessing `t` into a map of character positions can optimize subsequent queries.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_subsequence(s, t):
    if not s:
        return True
    s_pointer = 0
    for char in t:
        if char == s[s_pointer]:
            s_pointer += 1
        if s_pointer == len(s):
            return True
    return False
```

### Time Complexity:
`O(n)` where `n` is the length of `t`.

### Space Complexity:
`O(1)` as no extra space is used apart from pointers.

---

## Conclusion
The brute force and efficient approaches are the same in this case since they both achieve the optimal time complexity of `O(n)`. This problem highlights the importance of understanding subsequence verification and how to traverse sequences efficiently.
