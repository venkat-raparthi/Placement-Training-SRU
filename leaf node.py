class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def printLeafNodes(node):
    if node


    return

    if node.left is None and node.right is None:
        print(node.val)
        return
    
    if node.left:
        printLeafNodes(nodes.left)
    if node.right:
        printLeafNodes(node.right)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.right=TreeNode(6)
root.right.right.left=TreeNode(7)

printLeafNodes(root)