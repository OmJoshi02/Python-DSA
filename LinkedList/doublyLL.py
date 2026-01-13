class Node:
    def __init__(self ,data=None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, data):
        temp = Node(data)
        
        if(self.head == None):
            self.head = temp
            return
        else:
            
            t = self.head
            while (t.next != None):
                t = t.next
            t.next = temp
            temp.prev = t
            
    
    def insertAtBeg(self, data):
        temp = Node(data)
        
        if(self.head == None):
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        
    def insertAtMid(self,data,loc):
        temp = Node(data)
        t = self.head
            
        while(t.next != None):
            if(t.data == loc):
                break
            else:
                t = t.next
                
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t
        
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" <--> ")
            t1 = t1.next
        print(t1.data)
        
    def deletion(self, val):
        if(self.head == None):
            print("Linked List in Empty")
            return
        
        t = self.head
        if(t.data == val):
            self.head = t.next
            self.head.prev = None
            return
            
        while(t.next != None):
            if(t.data == val):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        if(t.data == val):
            t.prev.next = None
                

obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)

obj.insertAtBeg(40)

obj.insertAtMid(50, 20)

obj.deletion(40)
obj.printLL()