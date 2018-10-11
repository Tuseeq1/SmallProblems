"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_digits(self, l1, l2, carry):
        if not l2 and not l1:
            if carry == 0:
                return None
            cur = ListNode(carry)
            return cur

        elif not l2 and l1:
            carry, val = divmod((l1.val + carry), 10)
            cur = ListNode(val)
            cur.next = self.add_digits(l1.next, l2, carry)

            return cur
        elif not l1 and l2:
            carry, val = divmod((l2.val + carry), 10)
            cur = ListNode(val)
            cur.next = self.add_digits(l1, l2.next, carry)

            return cur

        carry, val = divmod((l1.val + l2.val + carry), 10)
        cur = ListNode(val)
        cur.next = self.add_digits(l1.next, l2.next, carry)

        return cur

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.add_digits(l1, l2, 0)
