
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prv = None

class LRUCache:

    
    def __init__(self, capacity: int):
        # dummy head and tail
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prv = self.head
        self.node_dict = {}
        self.cap = capacity

    def remove_node(self, node: Node):
        if node is None:
            return
        
        prv = node.prv
        nxt = node.nxt
        
        # prev to next
        prv.nxt = nxt
        nxt.prv = prv

        # remove node ref
        node.prv = None
        node.nxt = None

    def add_to_top(self, node):
        first = self.head.nxt
        # head link to node
        self.head.nxt = node
        node.prv = self.head

        # node link to first (second now)
        node.nxt = first
        first.prv = node

    def evictLast(self):
        before_tail = self.tail.prv
        if before_tail != self.head:
            self.remove_node(before_tail)
            del self.node_dict[before_tail.key] 

    def get(self, key: int) -> int:
        # not existing
        if key not in self.node_dict:
            return -1
        
    
        node = self.node_dict[key]
        self.remove_node(node)
        self.add_to_top(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        # just put new key value to map

        if key in self.node_dict:
            node = self.node_dict[key]
            node.value = value
            self.remove_node(node)
            self.add_to_top(node)
        else:
            node = Node(key, value)
            self.node_dict[key] = node
            self.add_to_top(node)

            if len(self.node_dict) > self.cap:
                self.evictLast()
        



      

        
        


        
