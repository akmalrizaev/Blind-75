## Two Sum II - Input Array Is Sorted (LeetCode #167)

### Understanding the Question
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers as an integer array `[index1, index2]` of length 2.

Inputs:
- `numbers`: List of integers sorted in non-decreasing order (e.g., `[2, 7, 11, 15]`).
- `target`: Integer (e.g., `9`).

Output:
- List of two integers `[index1, index2]` where `1 <= index1 < index2 <= numbers.length`.

Constraints:
- \(2 \leq \text{numbers.length} \leq 3 \times 10^4\)
- \(-1000 \leq \text{numbers[i]} \leq 1000\)
- `numbers` is sorted in non-decreasing order.
- Exactly one solution exists.

---

## Brute Force Approach

### Explanation:
Iterate through all pairs of elements and check if their sum equals the target. This approach is straightforward but inefficient for large arrays.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
```

### Time Complexity:
`O(n^2)` due to the nested loops.

### Space Complexity:
`O(1)` as no extra space is used.

---

## Efficient Solution

### Explanation:
Use the two-pointer technique:
1. Initialize two pointers, `left` at the beginning and `right` at the end of the array.
2. Calculate the sum of the elements at the two pointers.
3. If the sum equals the target, return the indices.
4. If the sum is less than the target, move the `left` pointer to the right.
5. If the sum is greater than the target, move the `right` pointer to the left.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

### Time Complexity:
`O(n)` as the array is traversed once with two pointers.

### Space Complexity:
`O(1)` since no additional space is used.

---

## Conclusion
The brute force approach checks all pairs of elements, which is inefficient for large inputs. The efficient solution uses the two-pointer technique to achieve linear time complexity while maintaining constant space, leveraging the sorted nature of the input array.
