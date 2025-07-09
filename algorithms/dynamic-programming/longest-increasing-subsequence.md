# Longest Increasing Subsequence

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples

### Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,18], therefore the length is 4.
```

### Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

### Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Constraints
- 1 ≤ nums.length ≤ 2500
- -10⁴ ≤ nums[i] ≤ 10⁴

## Approach

### Method 1: Dynamic Programming
**Key Insight:** For each position `i`, find the longest increasing subsequence ending at that position.

**Recurrence relation:** 
```
dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
```

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)

### Method 2: Binary Search + DP
Use a more efficient approach with binary search.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

## Solution Templates

### Python
```python
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Your solution here
    pass
```

### JavaScript
```javascript
function lengthOfLIS(nums) {
    // Your solution here
}
```

### Java
```java
public int lengthOfLIS(int[] nums) {
    // Your solution here
}
```

### C++
```cpp
int lengthOfLIS(vector<int>& nums) {
    // Your solution here
}
```

## Test Cases
```
lengthOfLIS([10,9,2,5,3,7,101,18]) → 4
lengthOfLIS([0,1,0,3,2,3]) → 4
lengthOfLIS([7,7,7,7,7,7,7]) → 1
lengthOfLIS([1,3,6,7,9,4,10,5,6]) → 6
lengthOfLIS([1]) → 1
lengthOfLIS([5,4,3,2,1]) → 1
```

## Visualization
For `nums = [10,9,2,5,3,7,101,18]`:

```
Index:     0  1  2  3  4  5   6   7
nums:    [10, 9, 2, 5, 3, 7, 101, 18]
dp:      [ 1, 1, 1, 2, 2, 3,  4,  4]

Explanation:
dp[0] = 1 (subsequence: [10])
dp[1] = 1 (subsequence: [9])
dp[2] = 1 (subsequence: [2])
dp[3] = 2 (subsequence: [2,5])
dp[4] = 2 (subsequence: [2,3])
dp[5] = 3 (subsequence: [2,3,7] or [2,5,7])
dp[6] = 4 (subsequence: [2,3,7,101] or [2,5,7,101])
dp[7] = 4 (subsequence: [2,3,7,18] or [2,5,7,18])
```

## Algorithm Steps (DP Approach)

1. Initialize `dp` array where `dp[i]` represents the length of LIS ending at index `i`
2. Set all `dp[i] = 1` (each element forms a subsequence of length 1)
3. For each position `i`, check all previous positions `j`:
   - If `nums[j] < nums[i]`, update `dp[i] = max(dp[i], dp[j] + 1)`
4. Return the maximum value in `dp` array

## Binary Search Approach (Advanced)

Instead of keeping track of all LIS lengths, maintain an array that stores the smallest tail element for each possible LIS length.

```python
def lengthOfLIS_optimized(nums):
    tails = []
    for num in nums:
        # Binary search to find the position to replace
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements, append it
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)
```

## Follow-up Questions
1. Can you return the actual longest increasing subsequence, not just its length?
2. What if you need to find the longest decreasing subsequence?
3. What if you want the longest non-decreasing subsequence (allowing equal elements)?

## Tags
`Dynamic Programming` `Array` `Binary Search` `LeetCode Medium`

## Related Problems
- Increasing Triplet Subsequence
- Russian Doll Envelopes
- Maximum Length of Pair Chain
- Number of Longest Increasing Subsequence
