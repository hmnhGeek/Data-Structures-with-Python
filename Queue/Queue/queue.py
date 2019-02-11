
import sys
sys.path.append('LinkedLists')

# import linked lists. we will use them to implement queue.
from LinkedLists import linked_lists

class Queue(object):

    ''' Queue implementation. Queue is FIFO. '''

    def __init__(self):
        self.queue = linked_lists.LinkedList()

    def isempty(self):
        ''' Returns True if queue is empty. '''
        if self.queue.head == None:
            return True
        else:
            return False

    def push(self, item):
        # let queue be s = [1,2,3,4]. Queue length is 4. Hence, insert item at queue length, which is 4, i.e. last position.
        self.queue.insert(item, self.queue.length())

    def pop(self):
        # check if queue is empty or not.
        if self.isempty():
            return "Queue is empty."
        else:
            # remember the FIFO order.
            retval = self.queue.access(0)
            self.queue.delete(0)
            return retval

    def top(self):
        if self.isempty():
            return None
        # the first element should be returned.
        return self.queue.access(0)

    def display(self):
        self.queue.printList()

    def ismember(self, item):
        if self.queue.search(item) != "Not found":
            return True
        else:
            return False
