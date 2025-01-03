## Contains Duplicate (LeetCode #217)

### Understanding the Question
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.

Inputs:
- `nums`: List of integers (e.g., `[1, 2, 3, 1]`).

Output:
- Boolean (`True` or `False`).

Constraints:
- \(1 \leq \text{nums.length} \leq 10^5\)
- \(-10^9 \leq \text{nums[i]} \leq 10^9\)

---

## Brute Force Approach

### Explanation:
Compare every pair of elements in the array to check for duplicates. Return `true` if a duplicate is found; otherwise, return `false` after all comparisons.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def contains_duplicate_brute_force(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

### Time Complexity:
`O(n^2)` because we check all pairs of elements.

### Space Complexity:
`O(1)` as no additional space is used.

---

## Efficient Solution

### Explanation:
Use a set to track elements as we iterate through the array. If an element already exists in the set, return `true`. Otherwise, add it to the set.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

### Time Complexity:
`O(n)` because we traverse the array once.

### Space Complexity:
`O(n)` for the set.

---

## Conclusion
The brute force approach checks all pairs to find duplicates, but it is computationally expensive. The efficient solution uses a set to achieve linear time complexity, making it more suitable for larger inputs. This problem highlights the advantage of using hash-based data structures like sets for efficient lookup operations.
