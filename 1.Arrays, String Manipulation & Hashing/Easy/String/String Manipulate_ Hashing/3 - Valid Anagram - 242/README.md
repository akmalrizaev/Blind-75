## Valid Anagram (LeetCode #242)

### Understanding the Question
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

Inputs:
- `s`: A string (e.g., "anagram").
- `t`: A string (e.g., "nagaram").

Output:
- Boolean (`True` or `False`).

Constraints:
- \(1 \leq \text{len}(s), \text{len}(t) \leq 5 \times 10^4\)
- `s` and `t` consist of lowercase English letters.

---

## Brute Force Approach

### Explanation:
Sort both strings and compare if they are equal. If they are, return `true`; otherwise, return `false`.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def is_anagram_brute_force(s, t):
    return sorted(s) == sorted(t)
```

### Time Complexity:
`O(n log n)` due to the sorting of both strings.

### Space Complexity:
`O(n)` for the sorted versions of the strings.

---

## Efficient Solution

### Explanation:
Use a hash map (or dictionary) to count the frequency of each character in `s` and `t`. Compare the two frequency dictionaries to check for equality.

### Python Code:
```python
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
```

### Time Complexity:
`O(n)` because we traverse both strings once to build frequency dictionaries.

### Space Complexity:
`O(n)` for the frequency dictionaries.

---

## Conclusion
The brute force approach relies on sorting, which is straightforward but slower for large inputs. The efficient solution uses hash maps to achieve linear time complexity. This problem demonstrates the importance of choosing the right data structure for optimal performance.