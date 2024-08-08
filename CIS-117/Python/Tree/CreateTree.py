
class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + f'\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode("Cold Drinks", [])
hot = TreeNode("Hot Drinks", [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode("tea", [])
coffee = TreeNode("coffee", [])
cola = TreeNode("cola", [])
fanta = TreeNode("fanta", [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)


print(tree)