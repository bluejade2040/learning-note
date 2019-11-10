#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Solution(object):
    def heap_sort(self, list):
        self.buildheap(list)
        n = len(list)
        for i in range(n-1,0,-1):
            list[0],list[i] = list[i],list[0] #最大值提出
            self.heapify(list, 0, i)
        return list
        
    def buildheap(self, list):
        n = len(list)
        for i in range(n,-1,-1):  #i從n到-1，每跑一次-1
            self.heapify(list, i, n)  #創造出最大值在root的heap
        
    def heapify(self, list, i, n): #建立子root為最大值 
    
        left = i*2+1
        right = i*2
    
        if left < n and list[left] > list[i]:
            lar = left
        else:
            lar = i
        if right < n and list[right] > list[lar]:
            lar = right
        if lar != i:  #判斷子根項是否最大，不是最大就替換掉  
            list[i],list[lar] = list[lar],list[i]
            self.heapify(list, lar, n)  #有替換就要再跑一次


Output = Solution().heap_sort([3,1,0,8,6,7,10,15,9,13,18,14])
Output

