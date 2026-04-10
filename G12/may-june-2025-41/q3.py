class Node:
    def __init__(self, NodeData):
        # self.NodeData : INTEGER
        # self.LeftNode : Node
        # self.RightNode : Node
        
        self.NodeData = NodeData
        self.LeftNode = None
        self.RightNode = None
        
    def GetLeft(self):
        return self.LeftNode
    
    def GetRight(self):
        return self.RightNode
    
    def GetData(self):
        return self.NodeData
    
    def SetLeft(self, newNode):
        # newNode : Node
        self.LeftNode = newNode
        
    def SetRight(self, newNode):
        # newNode : Node
        self.RightNode = newNode

class Tree:
    def __init__(self, FirstNode):
        # self.FirstNode : Node
        self.FirstNode = FirstNode
        
    def GetRootNode(self):
        return self.FirstNode
    
    def Insert(self, newNode):
        # newNode : Node
        CurrentNode = self.FirstNode
        isInserted = False
        
        while isInserted != True:
            if newNode.GetData() >= CurrentNode.GetData():
                if CurrentNode.GetRight() != None:
                    CurrentNode = CurrentNode.GetRight()
                else:
                    CurrentNode.SetRight(newNode)
                    isInserted = True
                    
            elif newNode.GetData() < CurrentNode.GetData():
                if CurrentNode.GetLeft() != None:
                    CurrentNode = CurrentNode.GetLeft()
                else:
                    CurrentNode.SetLeft(newNode)
                    isInserted = True

def OutputInOrder(NodeForCheck):
    if NodeForCheck.GetLeft() != None:
        OutputInOrder(NodeForCheck.GetLeft())
    
    print(NodeForCheck.GetData())
    
    if NodeForCheck.GetRight() != None:
        OutputInOrder(NodeForCheck.GetRight())

node1 = Node(10)
node2 = Node(20)
node3 = Node(5)
node4 = Node(15)
node5 = Node(7)

tree1 = Tree(node1)
tree1.Insert(node2)
tree1.Insert(node3)
tree1.Insert(node4)
tree1.Insert(node5)

OutputInOrder(tree1.GetRootNode())