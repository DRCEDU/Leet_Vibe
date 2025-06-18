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