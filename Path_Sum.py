
def helper(node , target):

    if node is None:
        return False 

    if  node.left == None and node.right == None:
        return target== node.value
    
    left = helper(node.left , target - node.value)
    right = helper(node.right , target - node.value)

    return left or right 
