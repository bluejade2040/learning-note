#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        for idx, element in enumerate(nums):
            sum_value = target - element
            if sum_value not in values:
                values[element] = idx
            else:
                return [values[sum_value], idx]

