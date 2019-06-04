# Ancestors in BST

class Node:
    def __init__(self,val,left=None,right=None,parent=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent
 
    def insert(self,val):
        if self==None:
            return
        if self.val>val:
            if self.left:
                self.left.insert(val)
                self.left.parent=self
            else:
                self.left=Node(val)
                self.left.parent=self
        else:
            if self.right:
                self.right.insert(val)
                self.right.parent=self
            else:
                self.right=Node(val)
                self.right.parent=self
 
    def traversal(self):
        if(self==None):
            return
        if self.left:
            self.left.traversal()
        print(self.val,end=" ")
        if self.right:
            self.right.traversal()
 
    def parentVal(self):
        if self==None:
            return
        else:
            if self.parent:
                return self.parent.val
            else:
                return -1
 
    def ancestor(self,val):
        if self==None:
            return "Empty Tree"
        present=False
        res=[]
        root=self
        while root:
            if root.val==val:
                present=True
                return res
            elif root.val>val:
                res.append(root.val)
                root=root.left
            else:
                res.append(root.val)
                root=root.right
        if present:
            return res
        else:
            return "Value not in Tree"
 
 
root=Node(10)
root.insert(11)
root.insert(13)
root.insert(9)
root.insert(12)
root.traversal()
print('\n')
 
print(root.ancestor(10))