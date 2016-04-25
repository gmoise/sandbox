class Node:
    def __init__ (self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

    def addElement(self,newElem):
        node = Node(newElem)
        self.nextNode = node
        node.prevNode = self
        return self.nextNode

    def deleteElement(self):
        parentNode = self.prevNode
        childNode = self.nextNode
        #connect parent with child
        parentNode.nextNode = childNode
        childNode.prevNode = parentNode
        

    def insertElement(self,newElem):
        node = Node(newElem)
        node.prevNode = self
        node.nextNode = self.nextNode
        self.nextNode.prevNode = node
        self.nextNode = node
        

    def switchElement (self):
        node1 = self.prevNode
        node2 = self
        node3 = self.nextNode
        node4 = node3.nextNode

        node3.prevNode = node1
        node3.nextNode = node2
        node2.prevNode = node3
        node2.nextNode = node4
        node1.nextNode = node3
        node4.prevNode = node2



root = Node("Barbeque")
nextNode1 = root.addElement("Chicken")
nextNode2 = nextNode1.addElement("Lemonade")
nextNode3 = nextNode2.addElement("Fries")
nextNode4 = nextNode3.addElement("Soda")
#nextNode2.deleteElement()
#nextNode5 = nextNode2.insertElement("Shoes")



node = root
while node:
    print (node.value)
    node = node.nextNode


nextNode2.switchElement()
print("*"*20)

node = root
while node:
    print (node.value)
    node = node.nextNode
