# Question: Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# def hasCycle(self, head):
    # input: head; output: boolean

    # Method 1: O(n)
    # seen = set()
    # curr = head
    # while curr:
    #     if curr in seen:
    #         return True
    #     seen.add(curr)
    #     curr = curr.next
    
    # return False

