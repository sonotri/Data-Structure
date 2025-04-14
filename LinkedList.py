class node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data  = data
        self.next = next

def node_insert(value, position):
    new_node = node(position, value, position.next)
    new_node.prev.next = new_node
    new_node.next.prev = new_node
    return new_node

def node_delete(input_node):
    input_node.prev.next = input_node.next
    input_node.next.prev = input_node.prev

def visit_all(input_node):
    now_node = input_node
    while True:
        print(now_node.data)
        now_node = now_node.prev
        if (now_node.data == None):
            break
