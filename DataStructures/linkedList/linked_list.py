# Node class represents an individual element in the list
from email import header


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# linked list is the class representing the list
class linkedList:
    def __init__(self):
        self.head = None

    # Insert at begining
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # Print function
    def print(self):
        if self.head == None:
            print('List is empty!')
            return
        iterator = self.head
        llstr = ''

        while iterator:
            llstr += str(iterator.data) + '==>'
            iterator = iterator.next

        print(llstr)

    # Insert in the end
    def insert_at_end(self, data):
        # When list is empty
        if self.head == None:
            self.head = Node(data, None)
            return
        # else
        itr = self.head
        # If next exits ,its not the end of the list. So keep traversing
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    # Takes values and creates list with them
    def insert_values(self, dataSet):
        self.head = None
        for data in dataSet:
            self.insert_at_end(data)

    # Takes a linked list and returns length of it
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # Removes a node from a particular index of a list
    def remove_from(self, index):
        # If index is out of bound of the list
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        # If index is the first , Just show it the next index
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            # We need to stop at the previous index
            if count == index - 1:
                # show it the next index
                itr.next = itr.next.next
                break

            itr = itr.next
            # manually maintaining count for linked list
            count = count + 1

    # Inserts an element at a given index
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index.")

        # utilize insert func created earlier
        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            # Stop at the previous element
            if count == index - 1:
                # Create a node with its next set to the next of the one we stopped at
                node = Node(data, itr.next)
                # Now, show the next node
                itr.next = node
                break

            itr = itr.next
            count = count + 1

    #Reverse a list
    def reverse(head):
        if head is None or head.next is None:
            return head
        
        rest = reverse(head.next)

        head.next.next = head
        head.next = None

        return rest

if __name__ == '__main__':
    ll = linkedList()
    # ll.insert_at_begining(45)
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(51)

    # ll.insert_at_end(54)
    # ll.insert_at_end(5)
    # ll.insert_at_end(42)

    ll.insert_values(["kola", "Aam", "Jaam", "Kathal", "lichu"])
    ll.print()
    ll.reverse()
    print("====After Reverse")
    ll.print()
    # print("Length: ", ll.get_length())
    # # ll.remove_from(3)
    # ll.insert_at(0, "dragonfruit")
    # ll.insert_at(3, "janina")
    # ll.print()
    # print("Length after removal: ", ll.get_length())

    # ll.insert_at_end("Jamburaaaa")
    # ll.print()
