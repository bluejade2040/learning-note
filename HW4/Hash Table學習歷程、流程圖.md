
# Hash Table學習歷程

### 測試套件


```python
from Crypto.Hash import MD5
h = MD5.new()
h.update("dog".encode("utf-8"))
print(h.hexdigest())
print(int(h.hexdigest(), 16))
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    

加密像是一個固定的程序，所以我想編寫新的def:hash用來處理加密


```python
def hash(key):
    h = MD5.new()
    h.update(str(key).encode("utf-8"))
    print(int(h.hexdigest(), 16))
hash("dog")
```

    9097202055026264535080901219663267845
    

流程圖:

![](https://github.com/bluejade2040/learning-note/blob/master/hash%20table.jpg)

釐清array、nodes的結構關係:

![](https://www.cs.wcupa.edu/rkline/assets/img/DS/chaining.gif?1317147325)

接下來開始逐步編寫各項功能~~

### 編寫add

第一步先建立add，並且把def:hash加入。

思考的時候發現index的設置不可或缺，採用餘數的方式分配array，並且運用linklist的概念做新增的動作，將原本的nodes接回新node。


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity #創造空間
        """
        :rtype: None
        """
        
    def hash(self, key): #加密的def
        h = MD5.new()
        h.update(str(key).encode("utf-8"))
        return int(h.hexdigest(), 16) #輸出value
    
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        idx = self.hash(key) % self.capacity #計算index的位置
        if self.data[idx] == None:  #原本這個index沒node
            self.data[idx] = ListNode(self.hash(key))
        else:                       #原本這個index有node
            cur = self.data[idx]
            self.data[idx] = ListNode(self.hash(key))
            self.data[idx].next = cur #把原本的node接到新node後
            
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
```

測試一下~~


```python
hashSet = MyHashSet()
hashSet.add("dog")
```

### 編寫contains

在建構contains時，我想先排除輸入值對應的array為空的情況。

若此array有值，走訪該array，看看有無輸入值。


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity #創造空間
        """
        :rtype: None
        """
    def hash(self, key): #加密的def
        h = MD5.new()
        h.update(str(key).encode("utf-8"))
        return int(h.hexdigest(), 16) #輸出value
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        while self.contains(key) is False: #當原本沒有要輸入的key
            idx = self.hash(key) % self.capacity #計算index的位置
            if self.data[idx] == None:  #原本這個index沒node
                self.data[idx] = ListNode(self.hash(key))
            else:                       #原本這個index有node
                cur = self.data[idx]
                self.data[idx] = ListNode(self.hash(key))
                self.data[idx].next = cur #把原本的node接到新node後
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        idx = self.hash(key) % self.capacity #計算index的位置
        if self.data[idx] == None: #該index為空
            return False
        else:
            cur = self.data[idx]
            while cur:
                if cur.val == self.hash(key): #已存在此value
                    return True
                else:
                    return False
                cur = cur.next #走訪此index
            return False
```

測試一下~~


```python
hashSet = MyHashSet()
hashSet.add("dog")
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("pig")
print(rel)
```

    True
    False
    

### 編寫remove

一開始同樣先確立index的位置，並且運用已寫好的contains來檢測要刪除的值是否存在此array中，若沒有則直接跳出。

接著判斷刪除值是否處於第一位，是的話就可以直接運用節點移除的方式進行刪除。

若不是，便運用走訪的方式找尋符合的節點進行刪除。


```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity #創造空間
        """
        :rtype: None
        """
    def hash(self, key): #加密的def
        h = MD5.new()
        h.update(str(key).encode("utf-8"))
        return int(h.hexdigest(), 16)  #輸出value
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        while self.contains(key) is False: #當原本沒有要輸入的key
            idx = self.hash(key) % self.capacity #計算index的位置
            if self.data[idx] == None:  #原本這個index沒node
                self.data[idx] = ListNode(self.hash(key))
            else:                       #原本這個index有node
                cur = self.data[idx]
                self.data[idx] = ListNode(self.hash(key))
                self.data[idx].next = cur #把原本的node接到新node後
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        idx = self.hash(key) % self.capacity #計算index的位置
        while self.contains(key) is True:  #確認有對應的值可刪
            cur = self.data[idx]
            if cur.val == self.hash(key):  #刪除值為第一個
                cur = cur.next
                self.data[idx] = cur
            else:  #刪除值為第一個之後
                while cur.next:
                    if cur.next.val == self.hash(key): #測到值
                        cur.next = cur.next.next
                    else:  #還沒測到
                        cur = cur.next


    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        idx = self.hash(key) % self.capacity #計算index的位置
        if self.data[idx] == None: #該index為空
            return False
        else:
            cur = self.data[idx]
            while cur:
                if cur.val == self.hash(key): #已存在此value
                    return True
                else:
                    return False
                cur = cur.next #走訪此index
            return False #當cur = None
```

最後測試~~


```python
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("dog")
rel = hashSet.contains("dog")
print(rel)
```

    True
    True
    False
    True
    False
    

參考資料:

https://www.cs.wcupa.edu/rkline/ds/hash-sets.html

https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/

https://youtu.be/aZVNWYSR_sY
