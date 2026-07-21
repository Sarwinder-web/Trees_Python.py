def Good_Nodes(root):
    count = 0

    def helper(node , max_now):
        nonlocal count

        if node is None:
            return

        if node.value >= max_now:
            count += 1

        newMax = max(node.value , max_now)

        helper(node.left , newMax)
        helper(node.right , newMax)

        return None  
    
    helper(root,float("-inf"))
    return count 
        
