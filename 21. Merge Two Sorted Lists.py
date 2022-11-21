# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def append(self, listNode, val):
        listNode.next = ListNode(val)
        listNode = listNode.next
        return listNode
    
    def mergeTwoLists(self, a, b):
        """
        :type a: Optional[ListNode]
        :type b: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        outputListPrimary = ListNode()
        outputList = outputListPrimary
        while True:
            if a is None:
                while b != None:
                    outputList = self.append(outputList, b.val)
                    b = b.next
                return outputListPrimary.next
            if b is None:
                while a != None:
                    outputList = self.append(outputList, a.val)
                    a = a.next
                return outputListPrimary.next
            
            if (a.val <= b.val):
                outputList = self.append(outputList, a.val)
                a = a.next
            elif (a.val > b.val):
                outputList = self.append(outputList, b.val)
                b = b.next
    
    
    
    
    



if __name__ == "__main__":
    solutionObj = Solution()
    print(solutionObj.mergeTwoLists([1, 2, 3], [1, 8, 6]))