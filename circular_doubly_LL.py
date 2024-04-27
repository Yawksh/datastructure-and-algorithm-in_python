class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
class singlyll():
    def __init__(self):
      self.head=None
    def traversal(self):
        a=self.head
        startnode=a
        while a:
            print(a.data,end="-> ")
            a=a.next
            while a!=startnode:
                 print(a.data,end="-> ")
                 a=a.next
            print("null")
            break
        return
sll=singlyll()
n1=Node(5)
sll.head=n1
n1.prev=n1
n1.next=n1

n2=Node(6)
n1.next=n2
n2.prev=n1
n2.next=n1

n3=Node(7)
n3.prev=n2
n2.next=n3
n3.next=n1

n4=Node(8)
n4.prev=n3
n3.next=n4
n4.next=n1

n5=Node(10)
n5.prev=n4
n4.next=n5
n5.next=n1
sll.traversal()
