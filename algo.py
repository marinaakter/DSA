class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.val=value

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def add(self,val):
        node=Node(val)
        if self.tail is None:
            self.head=node
            self.tail=node
            self.size+=1
        else:
            self.tail.next=node
            node.prev=self.head
            self.tail=node
            self.size+=1

    def __remove_node(self,node):
        if node.prev in None:
            self.head=node.next
        else:
            node.prev.next=node.next
        if node.next is None:
            self.tail=node.prev
        else:
            node.next.prev=node.prev
       
        
    def remove(self,value):
        node= self.head
        while node is not None:
            if node.val==value:
                self.__remove_node(Node)
            node=node.next



    def __str__(self):
        vals=[]
        nodes=self.head
        while nodes is not None:
            vals.append(nodes.val)
            nodes=nodes.next
        return f"[{','.join(str(val) for val in vals)}]"


my_list=DoublyLinkedList()
my_list.add(1)
my_list.add(5)
my_list.add(2)
my_list.remove(5)
print(my_list)
