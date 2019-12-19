
# BFS、DFS學習歷程

### BFS、DFS原理比較

兩者相同的建立模式:

創建空list:set、stack、outcome，用來存放待排序的值和已排序的值

建立confirm以確認該節點的狀態(True、False)

將取出值標記True後回傳到outcome

BFS(廣度優先搜尋):

階層式的搜尋，將未排序list:set從頭開始搜尋

DFS(深度優先搜尋):

先從一條支線搜尋到底再返回，將未排序list:stack從尾開始搜尋

### 流程圖

![](https://github.com/bluejade2040/learning-note/blob/master/BFS%E3%80%81DFS.jpg)

### BFS過程


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): #從u指向v
        self.graph[u].append(v) 
  
    def BFS(self, s): #s指的是current點
        outcome = [] #結果
        
        set = []  #用來放已經找到的點
        set.append(s)  #將current點放入set
        
        confirm = [False] * (len(self.graph)) #用來確認點是否已被找到
        confirm[s] = True  #已確認，標註True 
        
        while set:
            
            s = set.pop(0)  #將第一個取出
            outcome.append(s)
            for i in self.graph[s]:
                
                if confirm[i] == False:
                    set.append(i)
                    confirm[i] = True
                    
        return outcome #輸出結果
        
    #def DFS(self, s):
        
```

### 測試一下~~


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.BFS(2))
```

    [2, 0, 3, 1]
    

### DFS過程

原本試想在迴圈的部分用另一個def統整看看，或許可以簡化自己的邏輯。

將空list放在init避免def之間的影響

但試過後發現，在遞迴時要將def DFS的值往下送會有衍伸問題需要解決，反而讓邏輯更加複雜。


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.stack = []
        self.outcome = []
        
    def addEdge(self,u,v): #從u指向v
        self.graph[u].append(v) 
  
    def BFS(self, s): #s指的是current點
        outcome = [] 
        
        set = []  #用來放已經找到的點
        set.append(s)  #將current點放入set
        
        confirm = [False] * (len(self.graph)) #用來確認點是否已被找到
        confirm[s] = True  #已確認，標註True 
        
        while set:
            
            s = set.pop(0)  #將第一個取出
            outcome.append(s)
            
            for i in self.graph[s]:
                
                if confirm[i] == False:
                    
                    set.append(i)
                    confirm[i] = True
                    
        return outcome
    
    def DFS(self, s):  #s指的是current點
        self.stack.append(s)
        confirm = [False] * (len(self.graph)) #用來確認點是否已被找到
        confirm[s] = True  #已確認，標註True
        self.DFS_loop(s, confirm)
        
        return self.outcome
    
    def DFS_loop(self, s, confirm):
        if self.stack:    
            
            p = self.stack.pop()  #將最後一個取出
            self.outcome.append(p)
            
            for i in self.graph[s]:
                
                if confirm[i] == False:
                    
                    self.stack.append(i)  #將還沒找到的點append
                    confirm[i] = True#並確認找過
                    
            self.DFS_loop(i, confirm)
```

### 測試一下~~


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.BFS(2))
print(g.DFS(2))
```

    [2, 0, 3, 1]
    [2, 3, 0]
    

最後決定還是承襲BFS的寫法，用一個def寫完比較直觀


```python
from collections import defaultdict 

class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.stack = []
        self.outcome = []
        
    def addEdge(self,u,v): #從u指向v
        self.graph[u].append(v) 
  
    def BFS(self, s): #s指的是current點
        outcome = [] 
        
        set = []  #用來放已經找到的點
        set.append(s)  #將current點放入set
        
        confirm = [False] * (len(self.graph)) #用來確認點是否已被找到
        confirm[s] = True  #已確認，標註True 
        
        while set:
            
            s = set.pop(0)  #將第一個取出
            outcome.append(s)
            
            for i in self.graph[s]: 
                
                if confirm[i] == False:
                    set.append(i)  #將還沒找到的點append
                    confirm[i] = True  #並確認找過
                    
        return outcome
    
    def DFS(self, s): #s指的是current點
        self.stack.append(s)
        confirm = [False] * (len(self.graph)) #用來確認點是否已被找到
        confirm[s] = True  #已確認，標註True
        
        while self.stack:
            
            s = self.stack.pop()  #將最後一個取出
            self.outcome.append(s)
            
            for i in self.graph[s]:
                
                if confirm[i] == False:
                    
                    self.stack.append(i)  #將還沒找到的點append
                    confirm[i] = True  #並確認找過
                    
        return self.outcome

```

### 最後測試~~


```python
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.BFS(2))
print(g.DFS(2))
```

    [2, 0, 3, 1]
    [2, 3, 0, 1]
    

參考來源:

http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html

https://youtu.be/GFlthbUd7LQ

https://www.javatpoint.com/breadth-first-search-algorithm
