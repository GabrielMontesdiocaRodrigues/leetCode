# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        retorno = ListNode()
        current_node1 = list1 
        current_node2 = list2 

        while current_node1 and current_node2 is not None : 

            print(current_node1.val)
            print(current_node2.val)

            if current_node1.val >= current_node2.val : 
                retorno.next = current_node1
                retorno.next = current_node2
            else :
                retorno.next = current_node2 
                retorno.next = current_node1
            
            current_node1 = current_node1.next
            current_node2 = current_node2.next

        return retorno 