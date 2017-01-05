class LinkedListNode:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        string_rep = 'LinkedListNode(item={0}' + \
                                    'left={1}, ' + \
                                    'right={2})'
        return string_rep.format(self.item, self.left, self.right)


class LinkedList:
    def __init__(self, init_items=None):
        self.length = 0
        if init_items:
            self.head = LinkedListNode(init_items[0])
            prev = self.head
            self.length += 1
            for item in init_items:
                curr = LinkedListNode(item, prev, None)
                prev = curr
                self.length += 1
            self.tail = curr
        else:
            self.head = None
            self.tail = None

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index < 0: # Allow negative indexing from end
            index = self.length + index
        if not traverse and index > self.length - 1:
            raise IndexError
        curr = self.head
        curr_index = 0
        while curr_index < index:
            curr = curr.right
            curr_index += 1
        return 
        
