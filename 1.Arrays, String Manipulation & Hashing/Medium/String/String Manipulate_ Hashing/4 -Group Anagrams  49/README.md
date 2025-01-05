## Group Anagrams (LeetCode #49)

### Understanding the Question
Given an array of strings `strs`, group the anagrams together. An anagram is a word formed by rearranging the letters of another, typically using all the original letters exactly once.

Inputs:
- `strs`: List of strings (e.g., `["eat", "tea", "tan", "ate", "nat", "bat"]`).

Output:
- List of lists, where each inner list contains grouped anagrams (e.g., `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`).

Constraints:
- \(1 \leq \text{strs.length} \leq 10^4\)
- \(0 \leq \text{strs[i].length} \leq 100\)
- `strs[i]` consists of lowercase English letters.

---

## Brute Force Approach

### Explanation:
Compare each string with all other strings to check if they are anagrams by sorting them. Group strings that are anagrams together.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^2 * k log k)
# Space Complexity: O(n * k)
def group_anagrams_brute_force(strs):
    groups = []
    visited = set()
    for i in range(len(strs)):
        if i in visited:
            continue
        group = [strs[i]]
        visited.add(i)
        for j in range(i + 1, len(strs)):
            if sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                visited.add(j)
        groups.append(group)
    return groups
```

### Time Complexity:
`O(n^2 * k log k)` because we compare each string pair and sort each string during comparison.

### Space Complexity:
`O(n * k)` for storing groups and visited elements.

---

## Efficient Solution

### Explanation:
Use a hash map to group strings by their sorted version as the key. Traverse the array, sort each string, and add it to the corresponding key in the hash map. Finally, return the values of the hash map.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
```

### Time Complexity:
`O(n * k log k)` because we sort each string.

### Space Complexity:
`O(n * k)` for the hash map.

---

## Conclusion
The brute force approach compares all string pairs, which is inefficient for large inputs. The efficient solution leverages a hash map to group anagrams based on their sorted versions, significantly reducing computation time. This problem emphasizes the use of hash maps for efficient grouping tasks.