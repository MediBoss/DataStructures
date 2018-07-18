
    # The node class
class Node:

    def __init__(self,data):
        self.data = Data
        self.next = None
        self.prev = None

        # The doubly linked list class
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # function that retruns a boolean value if the list is empty or not
    def isEmpty(self):
        return self.head == None

    # This function adds the data given at the end of the list
    def insertTail(self, data):
        new_node = Node(data)
        new_node.next = None
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def deleteTail(self):
        if self.isEmpty() == True:
            print "The List is Empty"
        else:
            temp_node = self.head
            self.tail = self.tail.prev
            self.tail.next = None
            return temp

        # This function adds the data given at the beginning of the list
    def insertHead(self, data):
        new_node = Node(data)
        if self.isEmpty() == True:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    #This function deletes the head Node from the list
    def deleteHead(self):
        temp_node = self.head
        self.head = self.head.next
        self.head.prev = None
        if self.isEmpty() == True:
            self.tail = None
            print "The List is Empty"
        return temp

    #This function deletes a Node from the list given a data
    def delete(self, data):
        if self.isEmpty() == True:
            print "The List is Empty"
            return
        else:
            temp_node = self.head
            while(temp_node.data != data):
                # looking for the node that has the data to be deleted
                temp_node = temp_node.next
            if temp_node == self.head:
                self.deleteHead()
            elif temp_node == self.tail:
                self.deleteTail()
            else:
                temp_node.prev.next = temp_node.next
                temp_node.next.prev = temp_node.prev
