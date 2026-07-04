class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode("10")
root.left = TreeNode("5")
root.right = TreeNode("20")

print(root.value)
print(root.left.value)
print(root.right.value)
