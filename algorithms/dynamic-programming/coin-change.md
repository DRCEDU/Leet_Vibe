# Coin Change

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## Examples

### Example 1:
```
Input: coins = [1,3,4], amount = 6
Output: 2
Explanation: 6 = 3 + 3
```

### Example 2:
```
Input: coins = [2], amount = 3
Output: -1
Explanation: Cannot make amount 3 with coins of denomination 2
```

### Example 3:
```
Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for amount 0
```

### Example 4:
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

## Constraints
- 1 ≤ coins.length ≤ 12
- 1 ≤ coins[i] ≤ 2³¹ - 1
- 0 ≤ amount ≤ 10⁴

## Approach

### Key Insight
This is a classic DP problem. For each amount, we try using each coin and take the minimum.

**Recurrence relation:** 
```
dp[amount] = min(dp[amount - coin] + 1) for all coins where coin ≤ amount
```

### Base Cases
- `dp[0] = 0` (0 coins needed for amount 0)
- `dp[i] = infinity` initially for all other amounts

### Time & Space Complexity
- **Time Complexity:** O(amount × coins.length)
- **Space Complexity:** O(amount)

## Solution Templates

### Python
```python
def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    # Your solution here
    pass
```

### JavaScript
```javascript
function coinChange(coins, amount) {
    // Your solution here
}
```

### Java
```java
public int coinChange(int[] coins, int amount) {
    // Your solution here
}
```

### C++
```cpp
int coinChange(vector<int>& coins, int amount) {
    // Your solution here
}
```

## Test Cases
```
coinChange([1,3,4], 6) → 2
coinChange([2], 3) → -1
coinChange([1], 0) → 0
coinChange([1,2,5], 11) → 3
coinChange([2,5,10,1], 27) → 4
coinChange([1,2,5], 100) → 20
```

## Visualization
For `coins = [1,2,5]`, `amount = 11`:

```
Amount:  0  1  2  3  4  5  6  7  8  9  10 11
dp:      0  1  1  2  2  1  2  2  3  3  2  3

Explanation:
dp[0] = 0 (base case)
dp[1] = 1 (use coin 1)
dp[2] = 1 (use coin 2)
dp[3] = 2 (use coins 2+1)
dp[4] = 2 (use coins 2+2)
dp[5] = 1 (use coin 5)
dp[6] = 2 (use coins 5+1)
...
dp[11] = 3 (use coins 5+5+1)
```

## Different Approaches

### 1. Bottom-Up DP (Tabulation)
Build up the solution from smaller amounts to larger amounts.

### 2. Top-Down DP (Memoization)
Use recursion with memoization starting from the target amount.

### 3. BFS Approach
Treat this as finding the shortest path in a graph.

## Follow-up Questions
1. What if you want to find the actual combination of coins used?
2. What if each coin can only be used once?
3. What if you want to count the number of ways to make the amount?

## Tags
`Dynamic Programming` `Array` `BFS` `LeetCode Medium`

## Related Problems
- Coin Change 2
- Perfect Squares
- Minimum Cost For Tickets
- Combination Sum IV
