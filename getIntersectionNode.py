# Question: Given the heads of two singly linked-lists headA and headB, 
# return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
# Output: Intersected at '8'

# def getIntersectionNode(self, headA, headB):
    # if not headA or not headB:
    #     return
    # pA , pB = headA, headB
    # while pA != pB:
    #     if pA:
    #         pA = pA.next
    #     else: 
    #         pA = headB
    #     if pB:
    #         pB = pB.next
    #     else: 
    #         pB = headA
    # return pA