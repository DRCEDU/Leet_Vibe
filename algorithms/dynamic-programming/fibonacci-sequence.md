# Fibonacci Sequence

## Problem Description
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The sequence typically starts with 0 and 1.

**Sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Write a function to find the nth Fibonacci number.

## Examples

### Example 1:
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
```

### Example 2:
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2
```

### Example 3:
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
```

## Constraints
- 0 ≤ n ≤ 30

## Approach

### 1. Naive Recursive Approach
- **Time Complexity:** O(2^n)
- **Space Complexity:** O(n)

### 2. Dynamic Programming (Memoization)
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

### 3. Dynamic Programming (Tabulation)
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

### 4. Optimized Space
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Solution Templates

### Python
```python
def fibonacci(n):
    # Your solution here
    pass
```

### JavaScript
```javascript
function fibonacci(n) {
    // Your solution here
}
```

### Java
```java
public int fibonacci(int n) {
    // Your solution here
}
```

### C++
```cpp
int fibonacci(int n) {
    // Your solution here
}
```

## Test Cases
```
fibonacci(0) → 0
fibonacci(1) → 1
fibonacci(5) → 5
fibonacci(10) → 55
```

## Tags
`Dynamic Programming` `Math` `Recursion` `Memoization`
