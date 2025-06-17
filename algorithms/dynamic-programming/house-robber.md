# House Robber

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

## Examples

### Example 1:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 2:
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

### Example 3:
```
Input: nums = [5,1,3,9]
Output: 14
Explanation: Rob house 1 (money = 5) and house 4 (money = 9).
Total amount you can rob = 5 + 9 = 14.
```

## Constraints
- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 400

## Approach

### Key Insight
For each house, you have two choices:
1. **Rob this house:** Take current house money + max money from houses before the previous house
2. **Don't rob this house:** Take the max money up to the previous house

**Recurrence relation:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

### Base Cases
- `dp[0] = nums[0]` (only one house, rob it)
- `dp[1] = max(nums[0], nums[1])` (choose the house with more money)

### Time & Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) with optimized approach

## Solution Templates

### Python
```python
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Your solution here
    pass
```

### JavaScript
```javascript
function rob(nums) {
    // Your solution here
}
```

### Java
```java
public int rob(int[] nums) {
    // Your solution here
}
```

### C++
```cpp
int rob(vector<int>& nums) {
    // Your solution here
}
```

## Test Cases
```
rob([1,2,3,1]) → 4
rob([2,7,9,3,1]) → 12
rob([5,1,3,9]) → 14
rob([2,1,1,2]) → 4
rob([5]) → 5
rob([1,2]) → 2
```

## Visualization
For `nums = [2,7,9,3,1]`:

```
Houses:  [2, 7, 9, 3, 1]
Index:    0  1  2  3  4

dp[0] = 2                    (rob house 0)
dp[1] = max(2, 7) = 7        (rob house 1)
dp[2] = max(7, 2+9) = 11     (rob houses 0,2)
dp[3] = max(11, 7+3) = 11    (don't rob house 3)
dp[4] = max(11, 11+1) = 12   (rob houses 0,2,4)
```

## Follow-up Questions
1. What if the houses are arranged in a circle? (House Robber II)
2. What if it's a binary tree instead of a linear array? (House Robber III)
3. What if you could rob at most k non-adjacent houses?

## Tags
`Dynamic Programming` `Array` `LeetCode Medium`

## Related Problems
- House Robber II
- House Robber III
- Delete and Earn
- Maximum Sum of Non-Adjacent Elements
