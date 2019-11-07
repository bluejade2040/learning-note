#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Solution(object):
    def merge(self, arr1, arr2):
        
        p = 0
        q = 0  #兩個arr的index
        sort = []
     
        while p<len(arr1) and q<len(arr2):  #還沒走訪到結尾
            if arr1[p] <= arr2[q]:   #把較小的append進sort[]
                sort.append(arr1[p])
                p = p+1
            else:
                sort.append(arr2[q])
                q = q+1
        
        sort += arr1[p:]  #若arr1有多，補上p之後的
        sort += arr2[q:]  #若arr2有多，補上q之後的
        return sort
    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr  #長度小於2，直接return
        mid = len(arr)//2
        arr1 = self.merge_sort(arr[:mid])  #前半段
        arr2 = self.merge_sort(arr[mid:])  #後半段
        return self.merge(arr1, arr2)
    
Output = Solution().merge_sort([3,1,0,8,6,7,10,15,9,13,18,14])
Output

