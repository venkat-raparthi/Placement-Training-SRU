class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head