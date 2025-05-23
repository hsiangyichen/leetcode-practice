# Question: You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# def mergeTwoLists(self, list1, list2):
    # input: 2 linked lists; output: linked list

    # Method 1: O(n+m)
    # head = ListNode()
    # curr = head

    # while list1 or list2:
    #     if not list1 and list2:
    #         curr.next = list2
    #         break
    #     elif not list2 and list1:
    #         curr.next = list1
    #         break  
    #     if list1.val < list2.val:
    #         curr.next = list1
    #         list1 = list1.next
    #     else:
    #         curr.next = list2
    #         list2 = list2.next
    #     curr = curr.next
    # return head.next

    # Method 2: O(n+m)
    # head = ListNode()
    # curr = head

    # while list1 and list2:
    #     if list1.val < list2.val:
    #         curr.next = list1
    #         list1 = list1.next
    #     else:
    #         curr.next = list2
    #         list2 = list2.next
    #     curr = curr.next
    # if list1:
    #     curr.next = list1
    # elif list2:
    #     curr.next = list2
    # return head.next

