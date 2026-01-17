class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next
    
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert_atEnd(self, value):

        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while( t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insert_aTBegging(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insert_AtMiddle(self, value, x):
        temp = Node(value)
        t1 = self.head

        while( t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1= t1.next 
    

    def deleteLL(self, value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
        while( t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        
        if(t1.data == value):
            prev.next = None


    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
    

obj = SinglyLinkedList()
obj.insert_atEnd(100)
obj.insert_atEnd(200)
obj.insert_atEnd(300)
obj.insert_aTBegging(50)
obj.insert_AtMiddle(150, 100)
obj.deleteLL(300)
obj.printLL()


        