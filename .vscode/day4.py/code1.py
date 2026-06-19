class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
Node1=Node(10)
Node2=Node(20)
# print(Node1.data)
# print(Node2.data)
Node1.data=30
Node1.next=Node2
Node1.next=None
print(Node1.data)
print(Node1.next)
Node3=Node(70)
Node2.next=Node1
print(Node3.data)