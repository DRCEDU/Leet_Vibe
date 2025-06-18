# Binary Tree Maximum Path Sum

## Problem Statement
Given a non-empty binary tree, find the maximum path sum. A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

**Example:**
```
Input: root = [-10,9,20,null,null,15,7]

      -10
      /  \
     9   20
         / \
        15  7

Output: 42
Explanation: The optimal path is 15 -> 20 -> 7, which sums to 42.
```

## Approach
This problem is best solved using a bottom-up dynamic programming approach (post-order traversal). At each node, compute the maximum gain from its left and right subtrees, and update the global maximum path sum.

### Steps:
1. Define a recursive function that computes the maximum gain from each subtree.
2. For each node, calculate the maximum path sum passing through it.
3. Update the global maximum if the current path sum is higher.
4. Return the maximum gain that can be extended to the parent.

## Python Solution Template
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')
    
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        # Compute max gain from left and right
        left_gain = max(helper(node.left), 0)
        right_gain = max(helper(node.right), 0)
        # Path sum including current node
        current_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_sum)
        # Return max gain to parent
        return node.val + max(left_gain, right_gain)
    
    helper(root)
    return max_sum
```

## Complexity Analysis
- **Time Complexity:** O(n), where n is the number of nodes in the tree (each node is visited once).
- **Space Complexity:** O(h), where h is the height of the tree (recursion stack).

## Variants
- Maximum path sum between any two leaves
- Maximum path sum from root to leaf

## Practice
- Try implementing the solution in another language (e.g., Java, C++)
- Modify the problem to return the path itself, not just the sum 

## Solution

### Explanation
We use a recursive helper function to compute the maximum gain from each subtree. At each node, we:
- Recursively compute the maximum gain from the left and right children (ignore negative gains by taking max with 0).
- The maximum path sum at the current node is the node's value plus the left and right gains.
- Update a global variable if this path sum is greater than the current maximum.
- Return the node's value plus the maximum of the left or right gain to the parent (since a path cannot branch upwards).

### Python Implementation
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')
    
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        # Ignore negative paths
        left_gain = max(helper(node.left), 0)
        right_gain = max(helper(node.right), 0)
        # Path sum including current node
        current_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_sum)
        # Return max gain to parent
        return node.val + max(left_gain, right_gain)
    
    helper(root)
    return max_sum

# Example usage:
if __name__ == "__main__":
    # Construct the tree: [-10,9,20,null,null,15,7]
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxPathSum(root))  # Output: 42 