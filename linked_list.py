class LinkedList():
    def __init__(self):
        self.nodeCount = 3
        self.head = 1
        self.tail = 3

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        else:
            i = 1
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
            return curr