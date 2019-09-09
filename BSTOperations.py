class Node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
        self.order=None

    def printNode(self):
        print("Node Val is",self.val)

    def insert(self,val):
        if self.val>val:
            if self.left==None:
                self.left=Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right==None:
                self.right=Node(val)
            else:
                self.right.insert(val)
    def inorder(self):
        if self==None:
            return
        if self.left:
            self.left.inorder()
        if self.right:
            self.right.inorder()
        if self.left is None and self.right is None:
            print(self.val,end=" ")

    def postOrder(self,res=[]):
        if self==None:
            return 
        if self.left:
            self.left.postOrder(res)
        if self.right:
            self.right.postOrder(res)
        if self.left is None and self.right is None:
            self.order=1
        else:
            self.order=max(self.right.order if self.right else 0,self.left.order if self.left else 0)+1
        res.append([self.val,self.order])
        print(self.val,self.order)

    def countNonLeafNodes(self,root):
        if root==None or (root.right is None and root.left is None):
            return 0
        return 1+ self.countNonLeafNodes(root.left)+ self.countNonLeafNodes(root.right)
        

    def min_maxLevelSum(self):
        if self==None:
            return
        nodes=[self]
        minSum=self.val
        maxSum=self.val
        currLevel=0
        minLevel=1
        maxLevel=1
        while(nodes):
            nextnodes=[]
            currLevelSum=0
            currLevel=currLevel+1
            for node in nodes:
                currLevelSum=currLevelSum+node.val
                if node.left:
                    nextnodes.append(node.left)
                if node.right:
                    nextnodes.append(node.right)
            if(currLevelSum<minSum):
                minSum=currLevelSum
                minLevel=currLevel
            if(currLevelSum>maxSum):
                maxSum=currLevelSum
                maxLevel=currLevel
            nodes=nextnodes

        print("Min Sum is: ",minSum)
        print("Min Sum Level is: ",minLevel)
        print("Max Sum is: ",maxSum)
        print("Max Sum Level is: ",maxLevel)


root = Node(10)
root.insert(11)
root.insert(5)
root.insert(6)
root.insert(7)

root.min_maxLevelSum()
root.inorder()
print("\n")
res=[]
root.postOrder(res)
print(res)
res.sort(key=lambda x:x[1])
for i in range(len(res)):
    print(res[i][0])

print("\n")
print("Count of Non Leaf Nodes is",root.countNonLeafNodes(root))