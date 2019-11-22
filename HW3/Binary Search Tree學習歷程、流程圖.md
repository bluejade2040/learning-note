
# BST學習歷程、流程圖

遵守一個原則
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)

### 建立BST::insert(新增資料)


```python
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

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
```


```python
root1 = TreeNode(5)
Solution().insert(root1,1)
Solution().insert(root1,8)
Solution().insert(root1,4)
Solution().insert(root1,-4)
Solution().insert(root1,0)
Solution().insert(root1,10)
Solution().insert(root1,7)
Solution().insert(root1,16)
Solution().insert(root1,4)
```




    <__main__.TreeNode at 0x22e63fc5cf8>



### 建立BST::PrintTree()--檢查tree底下的值，以值的大小排列


```python
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
    

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
```


```python
root1 = TreeNode(5)
Solution().insert(root1,1)
Solution().insert(root1,8)
Solution().insert(root1,4)
Solution().insert(root1,-4)
Solution().insert(root1,0)
Solution().insert(root1,10)
Solution().insert(root1,7)
Solution().insert(root1,16)
Solution().insert(root1,4)
root1.PrintTree()
```

    -4
    0
    1
    4
    4
    5
    7
    8
    10
    16
    

### 建立BST::search(搜尋資料)


```python
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
    

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root == None : 
            return root  #root是None,回傳None
        if root.val == target:
            return root  #root是target回傳target
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
```


```python
Solution().search(root1,8)
```




    <__main__.TreeNode at 0x22e63f9e198>



### 建立BST::minNode()--找出最小結點，為delete做準備


```python
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
        if target >= root.val: 
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
```

### 建立BST::delete(刪除資料)


```python
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
        if target >= root.val: 
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
```

##### 加入PrintTree()檢查數值~~


```python
Solution().delete(root1,8)
root1.PrintTree()
```

    -4
    0
    1
    4
    4
    5
    7
    10
    

### 建立BST::modify(修改資料)


```python
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
        if target >= root.val: 
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
```


```python
Solution().search(root1,8)
Solution().delete(root1,8)
Solution().modify(root1,0,8)
root1.PrintTree()
```

    -4
    1
    4
    4
    5
    7
    8
    10
    


```python

流程圖:![]("https://github.com/bluejade2040/learning-note/blob/master/BST.jpg")

參考資料:
    https://gist.github.com/jakemmarsh/8273963
    https://youtu.be/7vw2iIdqHlM
    https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be
    https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    https://www.itread01.com/content/1542339850.html
    https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm
    https://www.laurentluce.com/posts/binary-search-tree-library-in-python/
```
