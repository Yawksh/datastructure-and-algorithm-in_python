class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class singlyll():
    def __init__(self):
      self.head=None
    def traverse(self):
        a=self.head
        while a:
            print(a.data,end=" ->")
            a=a.next
            while a !=self.head:
                  print(a.data,end="-> ")
                  a=a.next
            #print("null")    
            break
        print("null")
        
sll=singlyll()
n1=Node(5)

sll.head=n1
n1.next=sll.head

n2=Node(7)
n1.next=n2
n2.next=sll.head

n3=Node(8)
n2.next=n3
n3.next=sll.head
sll.traverse() 

#out put 5 ->7-> 8-> null
