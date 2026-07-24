class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

root = TreeNode(15)
root.left = TreeNode(8)
root.right = TreeNode(25)

def helper(node,lower,upper):

    if node is None:
        return True 
    
    if node.value <= lower or node.value >= upper:
        return False 

    lower_check = helper(node.left,lower,node.value)

    upper_check = helper(node.right,node.value,upper)

    return lower_check and upper_check

print(helper(root, float("-inf"), float("inf")))



