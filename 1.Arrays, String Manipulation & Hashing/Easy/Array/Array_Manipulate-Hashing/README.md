## Two Sum (LeetCode #1)

### Understanding the Question
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. Each input would have exactly one solution, and you may not use the same element twice.

Inputs:
- `nums`: List of integers (e.g., `[2, 7, 11, 15]`)
- `target`: An integer (e.g., `9`)

Output:
- Indices of the two numbers (e.g., `[0, 1]` for the above example).

Constraints:
- Each input would have exactly one solution.
- The same element cannot be used twice.

---

## Brute Force Approach

### Explanation:
Iterate through all pairs of elements in the array and check if their sum equals the `target`. If a pair is found, return their indices.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### Time Complexity:
`O(n^2)` because we check all pairs of elements in the array.

### Space Complexity:
`O(1)` as we do not use extra space apart from variables.

---

## Efficient Solution

### Explanation:
Use a hash map to store the difference (`target - nums[i]`) and the index of the current number as we iterate through the array. For each number, check if it exists in the hash map. If found, return the stored index and the current index.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            return [seen[num], i]
        seen[target - num] = i
```

### Time Complexity:
`O(n)` because we traverse the array once.

### Space Complexity:
`O(n)` for the hash map.

---

## Conclusion
The brute force approach solves the problem by checking all pairs, but it is computationally expensive. The efficient solution leverages a hash map to achieve linear time complexity, making it much faster for large inputs. This problem demonstrates the importance of using data structures like hash maps to optimize search operations.