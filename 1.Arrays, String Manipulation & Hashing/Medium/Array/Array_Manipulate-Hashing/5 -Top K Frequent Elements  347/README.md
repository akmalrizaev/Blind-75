## Top K Frequent Elements (LeetCode #347)

### Understanding the Question
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

Inputs:
- `nums`: List of integers (e.g., `[1, 1, 1, 2, 2, 3]`).
- `k`: An integer representing the number of top frequent elements to return (e.g., `2`).

Output:
- List of `k` most frequent elements (e.g., `[1, 2]`).

Constraints:
- \(1 \leq \text{nums.length} \leq 10^5\)
- \(-10^4 \leq \text{nums[i]} \leq 10^4\)
- \(1 \leq k \leq 	ext{unique elements in nums}\)

---

## Brute Force Approach

### Explanation:
Count the frequency of each element using a dictionary, then sort the elements by frequency and return the top `k` elements.

### Python Code:
```python
# Brute Force Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def top_k_frequent_brute_force(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    sorted_elements = sorted(freq, key=freq.get, reverse=True)
    return sorted_elements[:k]
```

### Time Complexity:
`O(n log n)` due to sorting the elements by frequency.

### Space Complexity:
`O(n)` for the frequency dictionary.

---

## Efficient Solution

### Explanation:
Use a hash map to count the frequencies of elements. Then, use a heap to efficiently get the `k` most frequent elements.

### Python Code:
```python
# Efficient Solution
# Time Complexity: O(n log k)
# Space Complexity: O(n + k)
import heapq

def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [element for element, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
```

### Time Complexity:
`O(n log k)` because we use a heap of size `k`.

### Space Complexity:
`O(n + k)` for the frequency dictionary and the heap.

---

## Conclusion
The brute force approach sorts the elements by frequency, which is less efficient for large inputs. The efficient solution uses a heap to maintain the top `k` elements, achieving better performance for large datasets. This problem showcases the importance of using appropriate data structures like heaps for optimal performance in selection problems.
