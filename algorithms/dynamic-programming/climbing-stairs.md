# Climbing Stairs

## Problem Description
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Examples

### Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top:
1. 1 step + 1 step
2. 2 steps
```

### Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### Example 3:
```
Input: n = 4
Output: 5
Explanation: There are five ways to climb to the top:
1. 1+1+1+1
2. 1+1+2
3. 1+2+1
4. 2+1+1
5. 2+2
```

## Constraints
- 1 ≤ n ≤ 45

## Approach

### Key Insight
This is essentially a Fibonacci problem! To reach step `n`, you can either:
- Come from step `n-1` and take 1 step
- Come from step `n-2` and take 2 steps

Therefore: `ways(n) = ways(n-1) + ways(n-2)`

### Base Cases
- `ways(1) = 1` (only one way to reach step 1)
- `ways(2) = 2` (two ways to reach step 2)

### Time & Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) with optimized approach

## Solution Templates

### Python
```python
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # Your solution here
    pass
```

### JavaScript
```javascript
function climbStairs(n) {
    // Your solution here
}
```

### Java
```java
public int climbStairs(int n) {
    // Your solution here
}
```

### C++
```cpp
int climbStairs(int n) {
    // Your solution here
}
```

## Test Cases
```
climbStairs(1) → 1
climbStairs(2) → 2
climbStairs(3) → 3
climbStairs(4) → 5
climbStairs(5) → 8
```

## Follow-up Questions
1. What if you could take 1, 2, or 3 steps at a time?
2. What if each step had a different cost and you wanted to find the minimum cost?
3. What if some steps were blocked?

## Tags
`Dynamic Programming` `Math` `Memoization` `LeetCode Easy`

## Related Problems
- House Robber
- Fibonacci Number
- Min Cost Climbing Stairs
