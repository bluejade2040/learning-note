#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if self.length - 1 < index < 0:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        if self.head is None:
            tmp = ListNode(val)
            self.head = tmp
        else:
            tmp = ListNode(val)
            tmp.next = self.head
            self.head = tmp
        self.length += 1

    def addAtTail(self, val):
        if self.head is None:
            tmp = ListNode(val)
            self.head = tmp
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            tmp = ListNode(val)
            cur.next = tmp
        self.length += 1

    def addAtIndex(self, index, val):
        if self.length < index < -2:
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index == 0 or index == -1:
            self.addAtHead(val)
            return
        cur = self.head
        for _ in range(index-1):
            cur = cur.next
        tmp = ListNode(val)
        tmp.next = cur.next
        cur.next = tmp
        self.length += 1

    def deleteAtIndex(self, index):
        if self.length - 1 < index < 0:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        cur = self.head
        for _ in range(index-1):
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        self.length -= 1

