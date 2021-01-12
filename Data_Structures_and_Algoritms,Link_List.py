class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print('The linkedlist is empty')
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    # Creating a method to insert the values in linked_list by passing a list as argument
    def insert_values(self,data_list):
        self.data = None
        for data in data_list:
            self.insert_at_end(data)

    # Creating a function to count the length of the link_list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Removing the dat at given index
    def remove_at(self,index):
        if index<0 or index>=self.get_length(): # Here it will check if the index is out of the limit
            raise Exception('Invalid Index')
        if index==0:
            self.head = self.head.next  # At this location the head at the first element of the list, it will shift to the
                                        # next element
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next # Now the basic idea to remove the element in the link list is to remove from its
                                        # addresses and replace with the addresses with the next element
                break
            itr = itr.next
            count += 1
    def insert_at (self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception ('Invalid Index')
        if index==0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1



if __name__ == '__main__':

    ll = LinkedList()
    
    #ll.insert_at_begining(4)
    #ll.insert_at_begining(8)
    #ll.insert_at_begining(19)
    #ll.insert_at_end(23)
    #ll.insert_at_end(63)
    #ll.insert_at_end(43)
    ll.insert_values(["rahul","gunja","kishan","sonal","ashutosh"])
    #ll.remove(-21)
    ll.insert_at(0,'Ashwin')
    ll.insert_at(2, 'gunja_ka_bhai')
    ll.print()
    #print('the length of the string is',ll.get_length())
