class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insert_atEnd(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next  
        t.next = temp
        temp.prev = t
    
    def insert_atBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    def insert_atMid(self, value, x):
        t = self.head

        while( t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        
        temp = Node(value)
        temp.next = t.next
        temp.prev = t
        t.next.prev = temp
        t.next = temp
    
    def deletion_LL(self, value):
        t = self.head
        if(t.data == value):
            self.head = t.next 
            self.head.prev = None
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            
            t = t.next
        if(t.data == value):
            t.prev.next = None
    
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = DoublyLL()
obj.insert_atBeg(5)
obj.insert_atEnd(10)
obj.insert_atEnd(20)
obj.insert_atEnd(30)
obj.insert_atEnd(40)
obj.insert_atBeg(2)
obj.insert_atMid(25, 20)
obj.deletion_LL(40)
obj.printLL()











