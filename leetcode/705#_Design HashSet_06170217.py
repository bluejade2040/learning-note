#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        for i in range(0,1000000):
            self.list.append(None)

    def add(self, key: int) -> None:
        if self.contains(key) is not True:
            self.list[key-1] = key

    def remove(self, key: int) -> None:
        if self.contains(key) is True:
            self.list[key-1] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bool = self.list[key-1] is not None
        return bool

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

