# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1
        s1 = []
        s2 = []

        while temp != None:
            s1.append(temp.val)
            temp = temp.next

        temp = l2
        while temp != None:
            s2.append(temp.val)
            temp = temp.next

        res = int(''.join([str(x) for x in s1[::-1]])) + int(''.join([str(x) for x in s2[::-1]]))
        res = [int(x) for x in str(res)]

        l3 = None
        for i in range(len(res)):
            new_node = ListNode(res[i])
            new_node.next = l3
            l3 = new_node

        return l3
        


