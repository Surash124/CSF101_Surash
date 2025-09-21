'''class stack:
    def __init__(self):
        self.items = [10,20,30,]

    def push(self, item):
        self.items.append(item)

    def pop(self):
       return self.items.pop()

stack = stack()
popped = stack.pop()
print(popped)
print(stack.items)'''


'''def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(1))
A = input(int(print("t")))
B = input(int(print("y")))
C=input(int(Print("u")))

x = (A + B + C)/3
print(x)
while x < 0:
    print("it's a negative integer")
else:
    print("its possitive int")

class TreeNodes:
    def __init__ (self,val):
        self.val = val
        self.left= None
        self.right = None

Root = TreeNodes(1)
Root.left = TreeNodes(2)    
Root.right = TreeNodes(3)
Root.left.left = TreeNodes(4)   
Root.right.right= TreeNodes(5)
print(Root.val)
print(Root.left.val)
print(Root.right.val)
print(Root.left.left.val)
print(Root.right.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
inorder(Root).val
print(Root.right.right.val)

def preorder(Root):
    if Root:
        print(Root.val)
        preorder(Root.left)
        preorder(Root.right)
preorder(Root).val
print(Root.right.right.val)'''

def insert(root,key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
            root.left = insert(root.left,key)
    if key > root.val:
            root.right = insert(root.right,key)
    return root
root = None
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
print(root.val)
root = insert(70)
print(root.right.val)
root = insert(60)