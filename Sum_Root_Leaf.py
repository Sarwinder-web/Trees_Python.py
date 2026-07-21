def Sum_Root_Leaf(root):

    answer = 0
    
    def helper(node , currentNumber):

        nonlocal answer
         
        if node is None:
            return None

        currentNumber = currentNumber*10 + node.value

        if node.left is None and node.right is None:
            answer +=  currentNumber
            return 
        
        helper(node.left , currentNumber)
        helper(node.right , currentNumber)

        return None 
    
    helper(root,0)
    return answer

    
