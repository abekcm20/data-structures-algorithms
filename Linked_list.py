class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data)+','
            itr = itr.next
        print(ll)
    def count_ll(self): 
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head 
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head 
        while itr.next:
            itr = itr.next 
        itr.next = Node(data, None)
    def remove_ll(self, index):
        if index<0 or index >= self.count_ll():
            raise Exception('Invalid index')
        if index==0:
            self.head = self.head.next 
            return
            
        count = 0
        itr = self.head 
        while itr:
            if count == index-1:
                itr.next = itr.next.next 
                break
            itr = itr.next 
            count += 1
    def inser_index(self, index, data):
        if index<0 or index >= self.count_ll():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data)
            return
        itr = self.head 
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next 
            count += 1
            
linkl = LinkedList()
linkl.insert_at_begining(3)
linkl.insert_at_begining(12)
linkl.insert_at_end(35)
linkl.insert_at_end(62)
linkl.remove_ll(2)
linkl.inser_index(2, 42)
linkl.print()
print(linkl.count_ll())