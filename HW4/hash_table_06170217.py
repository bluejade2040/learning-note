#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    def hash(self, key):
        h = MD5.new()
        h.update(str(key).encode("utf-8"))
        return int(h.hexdigest(), 16)
    def add(self, key):
        while self.contains(key) is False:
            idx = self.hash(key) % self.capacity
            if self.data[idx] == None:
                self.data[idx] = ListNode(self.hash(key))
            else:
                cur = self.data[idx]
                self.data[idx] = ListNode(self.hash(key))
                self.data[idx].next = cur
    def remove(self, key):
        idx = self.hash(key) % self.capacity
        while self.contains(key) is True:
            cur = self.data[idx]
            if cur.val == self.hash(key):
                cur = cur.next
                self.data[idx] = cur
            else:
                while cur.next:
                    if cur.next.val == self.hash(key):
                        cur.next = cur.next.next
                    else:
                        cur = cur.next
    def contains(self, key):
        idx = self.hash(key) % self.capacity
        if self.data[idx] == None:
            return False
        else:
            cur = self.data[idx]
            while cur:
                if cur.val == self.hash(key):
                    return True
                else:
                    return False
                cur = cur.next
            return False

