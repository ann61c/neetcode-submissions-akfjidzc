# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next        
        # dummy = ListNode(0, head)
        # curr = dummy.next
        # for i in range(1, left):
        #     if i == left - 1:
        #         pre = curr
        #     if i == left:
        #         start = curr
        #     curr = curr.next
        #     i += 1
        # return
        # prev = pre
        # curr = start
        # for i in range(left, right):
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node
        # prev.next = prev
        # start.next = curr
        # return dummt.next
            
        
        
        
        
        
        
        
        
        
        
        # counter = 1
        # mid_list = []
        # curr = head
        # while curr:
        #     if left <= counter <= right:
        #         mid_list.append(curr)
        #     curr = curr.next
        #     counter += 1
        # curr = head
        
        # reversed_mid = []
        # for node in mid_list:
        #     tmp = node
        #     node = node.next
        #     node.next = tmp
        #     reversed_mid.append(tmp)
        # return reversed_mid

        