# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        #Criacao da listnode de resposta
        dummy = ListNode()
        tail = dummy
        
        cur1 = list1
        cur2 = list2

        while (cur1 is not None) and (cur2 is not None):
            print(cur1.val)
            print(cur2.val)
            if cur1.val > cur2.val:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
                print("cur2", cur2)
            else:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next
                print("cur1", cur1)

        if cur1 is None:
            while cur2 is not None:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
                print("cur2", cur2)

        if cur2 is None:
            while cur1 is not None:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next
                print("cur1", cur1)
                
        # retorna sempre o proximo do tail
        return dummy.next

        