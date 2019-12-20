class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value) # creating new node with value

        if value < self.value: # if value is less than current node
            if self.left == None: # if left of current node is none
                self.left = node # set left to current node
            else:
                self.left.insert(value) # recursion on left side with value
        elif value > self.value: # if value is greater than current node
            if self.right == None: # if right of current node is none
                self.right = node # set right to current node
            else:
                self.right.insert(value) # recursion on right side with value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: # if target equals current node return True
            return True

        if target < self.value: # if target is less than node 
            if self.left: # check if left of node exists
                return self.left.contains(target) # recursion on left of node
            else:
                return False
        
        if target > self.value: # if target is more than node 
            if self.right: # check if right of node exists
                return self.right.contains(target) # recursion on right of node
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        max_node = self
        while max_node.right is not None: # while right of current node exists
            max_node = max_node.right # current node becomes right node
 
        return max_node.value
