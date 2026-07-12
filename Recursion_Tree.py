class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None 

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(5)
root.left.left = TreeNode(30)       

def maxDepth(node):

    if node is None:
        return 0

    left = maxDepth(node.left)

    right = maxDepth(node.right)

    return max(left, right) + 1

print(maxDepth(root))

# count nodes 
class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None 

root = TreeNode(10)
root.left = TreeNode(15)
root.right = TreeNode(5)
root.left.left = TreeNode(24) 

def count_nodes(node):

    if node is None:
        return 0 
    
    left = count_nodes(node.left)

    right = count_nodes(node.right)

    return left + right + 1

print(count_nodes(root))

# sum of nodes 
class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None 

root = TreeNode(10)
root.left = TreeNode(15)
root.right = TreeNode(5)
root.left.left = TreeNode(25) 

def sumNodes(node):

    if node is None:
        return 0
    
    left = sumNodes(node.left)

    right = sumNodes(node.right)

    return left + right + node.value

print(sumNodes(root))

# search prob
class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None 

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(5)
root.left.left = TreeNode(30)  

def search(node, target):

    if node is None:
        return False

    if node.value == target:
        return True

    left = search(node.left, target)
    right = search(node.right, target)

    return left or right

print(search(root,20))

# invert node 

class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

root = TreeNode(15)
root.left = TreeNode(8)
root.right = TreeNode(25)
root.left.left = TreeNode(13)
root.left.right = TreeNode(30)
root.right.right = TreeNode(35)
root.right.left = TreeNode(18) 

def preorder(node):
    if node is None:
        return

    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)
    
def invert(node):

    if node is None:
        return None

    invert(node.left)
    invert(node.right)

    node.left, node.right = node.right, node.left

    return node

invert(root)

preorder(root)

# same tree 
class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(4)

def sameTree(p,q):

    if p is None and q is None:
        return True 
    
    if p is None or q is None:
        return False
    
    if p.value != q.value:
        return False 
    
    return sameTree(p.left , q.left) and \
           sameTree(p.right , q.right)

print(sameTree(root1, root2))

# Balanced Tree 

class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

root = TreeNode(15)
root.left = TreeNode(8)
root.right = TreeNode(25)
root.left.left = TreeNode(13)
root.left.left.left = TreeNode(45)


def maxDepth(node):

    if node is None:
        return 0
    
    left = maxDepth(node.left)
    right = maxDepth(node.right)

    return max(left,right) + 1 

def isBalanced(node):
    if node is None:
        return True 
    
    leftHeight = maxDepth(node.left)
    rightHeight = maxDepth(node.right)

    leftBalanced = isBalanced(node.left)
    rightBalanced = isBalanced(node.right)

    return ( leftBalanced 
            and rightBalanced 
            and (leftHeight - rightHeight) <= 1
    )

print(isBalanced(root))

# balanced tree - other way to solve(interview style)

class TreeNode:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

root = TreeNode(15)
root.left = TreeNode(8)
root.right = TreeNode(25)
root.left.left = TreeNode(13)
root.left.left.left = TreeNode(45)

def helper(node):
    if node is None:
        return 0 , True 
    
    leftHeight , leftBalance = helper(node.left)
    rightHeight , rightBalance = helper(node.right)

    currentHeight = max(leftHeight,rightHeight) + 1
    currentBalance = ( leftBalance and 
                      rightBalance and
                        abs(leftHeight - rightHeight) <= 1)

    return currentHeight , currentBalance   

print(helper(root)) 
    

    



        

