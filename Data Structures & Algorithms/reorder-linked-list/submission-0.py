# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,  head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        second = slow.next #Start of second half of list 
        slow.next = None #Break connection between to halves 
        prev = None 

        #Reverse the second half of the list 
        while second: 
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp 
        
        #Merge the two halves 
        first, second = head, prev 
        #Second half usually runs out fasters, so run until valid
        while second:
            tmp1, tmp2 = first.next, second.next #Store connections
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2 


        