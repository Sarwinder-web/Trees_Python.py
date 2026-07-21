from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Creating tree
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def levelOrder(root):

    if root is None:
        return []

    queue = deque([root])
    answer = []

    while queue:

        level_size = len(queue)

        level = []

        while level_size > 0:

            node =  queue.popleft()

            level.append(node.value)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

            level_size -= 1

        answer.append(level)
    
    return answer 

result = levelOrder(root)

print(result)
            

