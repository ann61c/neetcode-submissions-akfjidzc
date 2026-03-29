"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        random_map = {}
        random_map[None] = None
        while curr:
            new_node = Node(curr.val)
            random_map[curr] = new_node
            curr = curr.next
        curr = head
        while curr:
            random_map[curr].next = random_map[curr.next]
            random_map[curr].random = random_map[curr.random]
            curr = curr.next

        return random_map[head]
        

        
        