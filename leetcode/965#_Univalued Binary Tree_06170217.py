#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root != None:
            if root.left!=None and root.val != root.left.val:
                return False
            elif root.right!=None and root.val != root.right.val:
                return False
        else:
            return True
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)

