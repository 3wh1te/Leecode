import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 超时
    def mergeKLists(self, lists) -> ListNode:
        res = None
        node = None
        while True:
            min = (0, lists[0])
            for index, head in enumerate(lists):
                if min[1] == None or (head != None and head.val <= min[1].val):
                    min = (index, head)
            index, head = min
            if head == None:
                return res

            if res == None:
                node = head
                res = node
            else:
                node.next = head
                node = node.next
            lists[index] = lists[index].next

def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def stringToIntegerList(input):
    return json.loads(input)

if __name__ == '__main__':
    lists = []
    input = ['[1,4,5]','[1,3,4]','[2,6]']
    for list in input:
        node = stringToListNode(list)
        prettyPrintLinkedList(node)
        lists.append(node)
    prettyPrintLinkedList(Solution().mergeKLists(lists))