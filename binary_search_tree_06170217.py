#!/usr/bin/env python
# coding: utf-8

# In[20]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()
            
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            return TreeNode(val)
        else:
            if val<=root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insert(root.left,val)
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    self.insert(root.right,val)
        return root
    
    def minNode(self, root): 
        cur = root 
   
        while(cur.left is not None): 
            cur = cur.left  
  
        return cur

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if not root:
            return None
        
        else:
            if root.val > target: 
                root.left = self.delete(root.left, target)

            elif root.val < target: 
                root.right = self.delete(root.right, target)

            else: 
                if not root.right:
                    temp = root.right  
                    root = None 
                    return temp

                if not root.left:
                    temp = root.left  
                    root = None
                    return temp
         
                temp = self.minNode(root.right) 
                root.val = temp.val 
                root.right = self.delete(root.right, temp.val)
        
        return root
    
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root == None : 
            return root
        if root.val == target:
            return root
        if target > root.val: 
            return self.search(root.right,target) 
        else:  
            return self.search(root.left,target)
        return root
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        while self.search(root, target):
            self.delete(root, target)
            self.insert(root, new_val)
            
        return root

