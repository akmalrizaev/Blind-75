## Longest Consecutive Sequence (LeetCode #128)

### Understanding the Question
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. The sequence must be consecutive integers, but the elements of the sequence can appear in any order in the array.

Inputs:
- `nums`: List of integers (e.g., `[100, 4, 200, 1, 3, 2]`).

Output:
- Integer representing the length of the longest consecutive sequence (e.g., `4` for the above input).

Constraints:
- \(0 \leq \text{nums.length} \leq 10^5\)
- \(-10^9 \leq \text{nums[i]} \leq 10^9\)

---

## Brute Force Approach

### Explanation:
Generate all possible subsets of consecutive sequences and find the longest one. This approach involves iterating over all elements and checking for consecutive elements by incrementing a counter.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def longest_consecutive_brute_force(nums):
    if not nums:
        return 0
    longest = 0
    for num in nums:
        current_num = num
        current_streak = 1
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1
        longest = max(longest, current_streak)
    return longest
```

### Time Complexity:
`O(n^2)` because for each element, we may traverse the array to find consecutive elements.

### Space Complexity:
`O(1)` as no extra space is used.

---

## Efficient Solution

### Explanation:
Use a hash set to store all numbers in the array for \(O(1)\) lookup. For each number, check if it is the start of a sequence (i.e., `num - 1` is not in the set). If it is the start, iterate through the sequence to determine its length.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def longest_consecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest = max(longest, current_streak)
    return longest
```

### Time Complexity:
`O(n)` because each number is visited and processed once.

### Space Complexity:
`O(n)` for the hash set.

---

## Conclusion
The brute force approach checks all possible sequences, leading to quadratic time complexity. The efficient solution leverages a hash set for constant-time lookups, reducing the time complexity to linear. This problem demonstrates the effectiveness of using hash sets for sequence-based problems.
