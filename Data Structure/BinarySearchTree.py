class binarySearchTree:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None
    def addChild(self,data):
        if data == self.data:
            return 
        #left child add
        if data < self.data:
            if self.left:
               self.left.addChild(data)
            else:
                self.left=binarySearchTree(data)
        if data > self.data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=binarySearchTree(data)
    def search(self,val):
        if self.data==val:
            return True
        if val< self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val> self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def inorderTreverse(self):
        elements=[]

        if self.left:
            elements+=self.left.inorderTreverse()
        
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorderTreverse()

        return elements
def buildTree(elements):
    root=binarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
        print(elements[i])

    return root


if __name__ == '__main__':
    

    numbers_tree = buildTree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.inorderTreverse())
    print(numbers_tree.search(7))


		


