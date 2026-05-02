"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored
in reverse order, and each of their nodes contains a single digit. Add the two numbers and return
the sum as a linked list. You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        str_to_print = ""
        while node:
            # print(node.val)
            str_to_print = str_to_print + str(node.val)
            # str += str(node.val)
            node = node.next
        return str_to_print

    def from_list(lst):
        head = ListNode(lst[0])
        node = head
        for el in lst[1:]:
            node.next = ListNode(el)
            node = node.next
        return head


def add_two_numbers(l1, l2):
    node1 = l1
    node2 = l2
    head = ListNode(0)

    current = head
    reminder = 0
    while node1 or node2 or reminder:
        v1 = node1.val if node1 else 0
        v2 = node2.val if node2 else 0
        current_sum = v1 + v2 + reminder
        reminder = current_sum // 10

        current.next = ListNode(current_sum % 10)
        current = current.next

        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next
    return head.next


def add_two_numbers_3(l1, l2):
    head = ListNode(0)
    node = head
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        node.next = ListNode(v1 + v2)
        node = node.next
        print(f"val1: {v1}, val2: {v2}, sum: {node.val}, head: {head}")
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        print("- - - ")
        # print(f"final_sum: {final_sum}")

    return head.next


def add_two_numbers_1(l1: ListNode, l2: ListNode) -> ListNode:
    final_sum = ListNode()
    remainder = 0
    final_sum.val = l1.val + l2.val
    l1 = l1.next
    l2 = l2.next
    while l1 and l2:
        print(f"l1: {l1.val}, l2: {l2.val}")
        s = l1.val + l2.val + remainder
        if s > 9:
            remainder = s // 10
            s = s % 10
        l1 = l1.next
        l2 = l2.next
        final_sum.next = s
        # final_sum.append(s)
    # print(f"l1: {l1}, l2: {l2}")
    if l1:
        while l1:
            final_sum.next = s
            # final_sum.append(l1.val)
            l1 = l1.next
    if l2:
        while l2:
            final_sum.next = l2.val
            l2 = l2.next
    print(f"- - {final_sum.val} - -")
    return final_sum


def add_two_numbers_0(l1, l2):
    final_sum = []
    remaining = 0
    for i in range(min(len(l1), len(l2))):
        k = l1[i] + l2[i] + remaining
        print(f"{i}: {k}")
        remaining = 0
        if k > 9:
            remaining = k // 10
            print(f"remaining: {remaining}")
            k = k % 10
        final_sum.append(k)
    return final_sum


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(2)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(9)
    print(f"l1: {l1}, l2: {l2}")
    res = add_two_numbers(l1, l2)
    print(f"res: {res}")
