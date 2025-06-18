# Dynamic Programming Problems Index

This folder contains various dynamic programming challenges organized by difficulty and topic. Each problem includes detailed explanations, multiple solution approaches, and code templates in different programming languages.

## 📚 Problems List

### Beginner Level
1. **[Fibonacci Sequence](./fibonacci-sequence.md)** - Classic introduction to DP
2. **[Climbing Stairs](./climbing-stairs.md)** - Understanding state transitions

### Intermediate Level
3. **[House Robber](./house-robber.md)** - Decision-based DP
4. **[Coin Change](./coin-change.md)** - Optimization problems

### Advanced Level
5. **[Longest Increasing Subsequence](./longest-increasing-subsequence.md)** - Subsequence problems

### Tree DP
6. **[Binary Tree Maximum Path Sum](./binary-tree-maximum-path-sum.md)** - Tree-based DP, finding the maximum path sum in a binary tree

## 🎯 Learning Path

### Phase 1: Fundamentals
Start with problems that have clear recurrence relations:
- Fibonacci Sequence
- Climbing Stairs

### Phase 2: Decision Making
Problems where you need to make optimal choices:
- House Robber
- Coin Change

### Phase 3: Complex States
Problems with more complex state definitions:
- Longest Increasing Subsequence

## 🔧 Common DP Patterns

### 1. Linear DP
- State depends on previous states in a sequence
- Examples: Fibonacci, Climbing Stairs, House Robber

### 2. Optimization DP
- Find minimum/maximum value
- Examples: Coin Change, Edit Distance

### 3. Counting DP
- Count number of ways to achieve something
- Examples: Unique Paths, Decode Ways

### 4. Subsequence DP
- Problems involving subsequences or substrings
- Examples: Longest Increasing Subsequence, Longest Common Subsequence

## 💡 DP Problem-Solving Framework

### Step 1: Identify if it's a DP problem
- Optimal substructure exists
- Overlapping subproblems
- Multiple ways to solve the same subproblem

### Step 2: Define the state
- What does dp[i] represent?
- What are the dimensions of your DP table?

### Step 3: Find the recurrence relation
- How does dp[i] relate to previous states?
- What are the base cases?

### Step 4: Implement
- Top-down (memoization) or Bottom-up (tabulation)?
- Consider space optimization

### Step 5: Optimize
- Can you reduce space complexity?
- Are there mathematical optimizations?

## 🚀 Implementation Approaches

### Top-Down (Memoization)
```python
def solve(n, memo={}):
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 1:
        return n
    
    # Recursive case
    memo[n] = solve(n-1, memo) + solve(n-2, memo)
    return memo[n]
```

### Bottom-Up (Tabulation)
```python
def solve(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### Space Optimized
```python
def solve(n):
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

## 📊 Complexity Analysis

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Fibonacci | O(n) | O(1) optimized |
| Climbing Stairs | O(n) | O(1) optimized |
| House Robber | O(n) | O(1) optimized |
| Coin Change | O(amount × coins) | O(amount) |
| LIS | O(n²) or O(n log n) | O(n) |

## 🔗 Related Topics
- Recursion
- Memoization
- Graph Algorithms
- Greedy Algorithms
- Mathematical Optimization

## 📝 Tips for Success
1. **Start Simple**: Begin with the recursive solution
2. **Identify Overlaps**: Look for repeated subproblems
3. **Choose Your Approach**: Top-down vs Bottom-up
4. **Optimize Space**: Look for patterns to reduce memory usage
5. **Practice Variants**: Try different versions of the same problem

## 🎯 Next Steps
After mastering these problems, consider exploring:
- 2D DP problems (Unique Paths, Edit Distance)
- String DP problems (Palindrome Partitioning)
- Tree DP problems (Binary Tree Maximum Path Sum)
- Interval DP problems (Matrix Chain Multiplication)
