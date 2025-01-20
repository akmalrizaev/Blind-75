## 3Sum (LeetCode #15)

### Understanding the Question
Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that \(i \neq j \neq k\), and \(nums[i] + nums[j] + nums[k] = 0\).

Inputs:
- `nums`: List of integers (e.g., `[-1, 0, 1, 2, -1, -4]`).

Output:
- List of unique triplets where the sum of each triplet equals zero (e.g., `[[-1, -1, 2], [-1, 0, 1]]` for the above input).

Constraints:
- \(3 \leq \text{nums.length} \leq 3000\)
- \(-10^5 \leq \text{nums[i]} \leq 10^5\)

---

## Brute Force Approach

### Explanation:
Iterate through all combinations of three elements in the array and check if their sum is zero. This approach is straightforward but inefficient due to the nested loops.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^3)
# Space Complexity: O(1)
def three_sum_brute_force(nums):
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(triplet) for triplet in result]
```

### Time Complexity:
`O(n^3)` due to the three nested loops.

### Space Complexity:
`O(m)` where `m` is the number of unique triplets.

---

## Efficient Solution

### Explanation:
Use sorting and a two-pointer technique:
1. Sort the array.
2. Iterate through the array with the first pointer.
3. For each fixed element, use two pointers (`left` and `right`) to find pairs that sum to the negative of the fixed element.
4. Skip duplicate elements to ensure unique triplets.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n^2)
# Space Complexity: O(m)
def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

### Time Complexity:
`O(n^2)` as the array is traversed with nested loops after sorting.

### Space Complexity:
`O(m)` where `m` is the number of unique triplets.

---

## Conclusion
The brute force approach checks all combinations of three elements, which is computationally expensive. The efficient solution leverages sorting and the two-pointer technique to achieve quadratic time complexity, demonstrating how optimizing the search space can improve performance significantly.
