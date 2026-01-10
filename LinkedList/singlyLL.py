class Node:
    
    def __init__(self,data,next=None): #next=None is used because if there is no next address then it is None by Default
        self.data = data
        self.next = next
        
        
class SinglyLL:
    def __init__(self, head=None): #head is none by default
        self.head = head
        
    def insertionAtBeg(self,val):
        temp = Node(val)
        
        temp.next = self.head 
        self.head = temp
    
    def insertInMid(self,val,loc):
        temp = Node(val);
        t1 = self.head
        
        while(t1.next != None):
            if(t1.data == loc):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
                
                
        
    def insertionAtEnd(self, val):
        temp = Node(val)
        
        #If linked List already present
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp 
        else:
            self.head = temp
    
    def deleteLL(self, val):
        t1 = self.head
        prev = t1
        
        if(t1.data == val):
            self.head = t1.next
            
        while(t1.next != None):
            if(t1.data == val):
                prev.next = t1.next
                break;
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == val):
            prev.next = None
        
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
obj = SinglyLL()

obj.insertionAtEnd(10)
obj.insertionAtEnd(20)
obj.insertionAtEnd(30)

obj.insertionAtBeg(50)

obj.insertInMid(40,20)

obj.deleteLL(30)
obj.printLL()