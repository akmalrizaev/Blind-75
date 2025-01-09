## Product of Array Except Self (LeetCode #238)

### Understanding the Question
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The solution must be done without using division and in \(O(n)\) time.

Inputs:
- `nums`: List of integers (e.g., `[1, 2, 3, 4]`).

Output:
- List of integers where each element is the product of all other elements (e.g., `[24, 12, 8, 6]` for the above input).

Constraints:
- \(2 \leq \text{nums.length} \leq 10^5\)
- \(-30 \leq \text{nums[i]} \leq 30\)
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

---

## Brute Force Approach

### Explanation:
Iterate through each element in the array and compute the product of all other elements by iterating through the array again. This approach is straightforward but inefficient for large inputs.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def product_except_self_brute_force(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result
```

### Time Complexity:
`O(n^2)` due to the nested loops.

### Space Complexity:
`O(1)` as no extra space is used other than the result list.

---

## Efficient Solution

### Explanation:
Use two passes with prefix and suffix products:
1. Create a `prefix` array where each element contains the product of all elements to its left.
2. Create a `suffix` array where each element contains the product of all elements to its right.
3. Combine the prefix and suffix products to compute the result.

This can be optimized further to use only \(O(1)\) extra space by modifying the result array in place.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Compute prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and combine
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
```

### Time Complexity:
`O(n)` for traversing the array twice.

### Space Complexity:
`O(1)` extra space, as the result array does not count toward space complexity.

---

## Conclusion
The brute force approach is computationally expensive, making it unsuitable for large inputs. The efficient solution achieves linear time complexity with constant extra space by using prefix and suffix products. This problem illustrates the value of systematic array traversal to optimize performance.
