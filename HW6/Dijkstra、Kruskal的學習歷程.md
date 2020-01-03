
# Kruskal、Dijkstra學習歷程

## 原理比較

##### 最短路徑法 ~ Dijkstra’s shortest path :

一開始指定起始點，從距離起始點最近的(weight最小)的開始走訪，若遇到有更小的weight就取代。

直到所有節點都拜訪完，輸出起始點到各點的距離。

##### 最小生成樹 ~ Kruskal’s Minimum Spanning Tree :

一開始並無起始點，而是根據weight來排序所有輸入的addEdge，並且從weight最小的開始連結。

只要碰到有cycle的情況就跳過。最後輸出被採用的節點與距離u,v,w

### 流程圖

![](https://github.com/bluejade2040/learning-note/blob/master/Dijkstra.jpg)

### Kruskal


```python
from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []  #for Dijkstra裝gragh用
        self.graph_k = []  #for Kruskal裝gragh用
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #for Kruskal生成矩陣圖用
    def addEdge(self,u,v,w):  #從u到v，u=row，v=column，權重是w
        self.graph.append([u,v,w])
        
    #def Dijkstra(self, s): 
        
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def Kruskal(self): 
  
        result =[] #放置結果array
  
        i = 0 #用於排序
        e = 0 #用於結果list

        self.graph_k =  sorted(self.graph_k,key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
        dic = {}  #用於調整dict
        name = {} #用於調整dict

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      

        while e < self.V -1 : 

            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

        print(result)
        for u,v,weight  in result:  #新增至dic
            name = ('{}-{}').format(u,v)
            dic[name] = weight
        return dic
```


```python
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

print("Kruskal",g.Kruskal()) 
```

    [[0, 1, 10], [0, 2, 6], [0, 3, 5]]
    Kruskal {'0-1': 10, '0-2': 6, '0-3': 5}
    


```python
from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []  #for Dijkstra裝gragh用
        self.graph_k = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #for Kruskal生成矩陣圖用
    def addEdge(self,u,v,w):  #從u到v，u=row，v=column，權重是w
        self.graph_k.append([u,v,w])
    #def Dijkstra(self, s): 

    #def Kruskal(self):
        #edgeset = {}
        #subset  = [[-1 for column in range(self.V)]  
        #            for row in range(self.V)]
        #increaseW = [sorted()]
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def Kruskal(self): 
  
        result =[] #放置結果array
  
        i = 0 #用於排序
        e = 0 #用於結果list

        self.graph_k =  sorted(self.graph_k,key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
        dic = {}  #用於調整dict
        name = {} #用於調整dict

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      

        while e < self.V -1 : 

            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

        print(result)
        for u,v,weight  in result:  #新增至dic
            name = ('{}-{}').format(u,v)
            dic[name] = weight
        return dic
```


```python
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

print("Kruskal",g.Kruskal()) 
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-141-8ce615b465f7> in <module>
          6 g.addEdge(2, 3, 4)
          7 
    ----> 8 print("Kruskal",g.Kruskal())
    

    <ipython-input-140-4f8737a31bbc> in Kruskal(self)
         57         while e < self.V -1 :
         58 
    ---> 59             u,v,w =  self.graph[i]
         60             i = i + 1
         61             x = self.find(parent, u)
    

    IndexError: list index out of range


#### 修改一些小錯誤


```python
from collections import defaultdict 
  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = []  #for Dijkstra裝gragh用
        self.graph_k = []  #for Kruskal裝gragh用
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #for Kruskal生成矩陣圖用 
 
    def addEdge(self,u,v,w): #從u到v，u=row，v=column，權重是w  
        self.graph_k.append([u,v,w]) #從u到v，權重為w

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
 
    def Kruskal(self): 
  
        result =[] #放置結果array
  
        i = 0 #用於排序
        e = 0 #用於結果list

        self.graph_k =  sorted(self.graph_k,key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
        dic = {}  #用於調整dict
        name = {} #用於調整dict

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        while e < self.V -1 : 

            u,v,w =  self.graph_k[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

        for u,v,weight  in result:  #新增至dic
            name = ('{}-{}').format(u,v)
            dic[name] = weight
        return dic
```

#### 測試看看~~


```python
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

print("Kruskal",g.Kruskal()) 
```

    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
    

### Dijkstra


```python
from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []  #for Dijkstra裝gragh用
        self.graph_k = []  #for Kruskal裝gragh用
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #for Kruskal生成矩陣圖用
    def addEdge(self,u,v,w):  #從u到v，u=row，v=column，權重是w
        self.graph_matrix[u][v] = w
        self.graph_matrix[v][u] = w
    def Dijkstra(self, s): 
        walked=[]
        result={node:0 for node in range(self.V)}
        cur = s
        while len(walked)<self.V:
            walked.append(cur)
            can_walk =[(n,c) for n,c in enumerate(self.graph[cur]) if (c!=0)and(n not in walked)]
            if len(can_walk)!=0:
                next_node = can_walk[0]

            for n,c in can_walk:
                new_cost = result[cur]+c
                if (result[n]==0)or(new_cost<result[n]):
                    result[n] = new_cost
                elif result[n]+c<result[cur]:
                    result[cur]=result[n]+c
            search = [(n,c)for n,c in result.items() if (c!=0)and(n not in walked)]
            
            if len(search)!=0:
                next_node = search[0]
                for n,c in search:
                    if c <next_node[1]:
                        next_node = (n,c)
                cur = next_node[0] 
        result={str(k):v for k,v in result.items()}
        return result
        
```


```python
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
print("Dijkstra",g.Dijkstra(0))
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    

### 合併


```python
from collections import defaultdict 
  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = []  #for Dijkstra裝gragh用
        self.graph_k = []  #for Kruskal裝gragh用
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #for Kruskal生成矩陣圖用 
 
    def addEdge(self,u,v,w): #從u到v，u=row，v=column，權重是w  
        self.graph.append([u,v,w]) #從u到v，權重為w

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
            
    def Dijkstra(self, s): 
        walked=[]
        result={node:0 for node in range(self.V)}
        cur = s
        while len(walked)<self.V:
            walked.append(cur)
            can_walk =[(n,c) for n,c in enumerate(self.graph[cur]) if (c!=0)and(n not in walked)]
            if len(can_walk)!=0:
                next_node = can_walk[0]

            for n,c in can_walk:
                new_cost = result[cur]+c
                if (result[n]==0)or(new_cost<result[n]):
                    result[n] = new_cost
                elif result[n]+c<result[cur]:
                    result[cur]=result[n]+c
            search = [(n,c)for n,c in result.items() if (c!=0)and(n not in walked)]
            
            if len(search)!=0:
                next_node = search[0]
                for n,c in search:
                    if c <next_node[1]:
                        next_node = (n,c)
                cur = next_node[0] 
        result={str(k):v for k,v in result.items()}
        return result 
    
    def Kruskal(self): 
  
        result =[] #放置結果array
  
        i = 0 #用於排序
        e = 0 #用於結果list

        self.graph_k =  sorted(self.graph_k,key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
        dic = {}  #用於調整dict
        name = {} #用於調整dict

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        while e < self.V -1 : 

            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

        for u,v,weight  in result:  #新增至dic
            name = ('{}-{}').format(u,v)
            dic[name] = weight
        return dic
```


```python
from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []  #for Dijkstra裝gragh用
        self.graph_k = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] #for Kruskal生成矩陣圖用
    def addEdge(self,u,v,w):  #從u到v，u=row，v=column，權重是w
        self.graph_k.append([u,v,w])
    def Dijkstra(self, s): 
        walked=[]
        result={node:0 for node in range(self.V)}
        cur = s
        while len(walked)<self.V:
            walked.append(cur)
            can_walk =[(n,c) for n,c in enumerate(self.graph[cur]) if (c!=0)and(n not in walked)]
            if len(can_walk)!=0:
                next_node = can_walk[0]

            for n,c in can_walk:
                new_cost = result[cur]+c
                if (result[n]==0)or(new_cost<result[n]):
                    result[n] = new_cost
                elif result[n]+c<result[cur]:
                    result[cur]=result[n]+c
            search = [(n,c)for n,c in result.items() if (c!=0)and(n not in walked)]
            
            if len(search)!=0:
                next_node = search[0]
                for n,c in search:
                    if c <next_node[1]:
                        next_node = (n,c)
                cur = next_node[0] 
        result={str(k):v for k,v in result.items()}
        return result 

    #def Kruskal(self):
        #edgeset = {}
        #subset  = [[-1 for column in range(self.V)]  
        #            for row in range(self.V)]
        #increaseW = [sorted()]
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 

        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    def Kruskal(self): 
  
        result =[] #放置結果array
  
        i = 0 #用於排序
        e = 0 #用於結果list

        self.graph_k =  sorted(self.graph_k,key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
        dic = {}  #用於調整dict
        name = {} #用於調整dict

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      

        while e < self.V -1 : 

            u,v,w =  self.graph_k[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             

        for u,v,weight  in result:  #新增至dic
            name = ('{}-{}').format(u,v)
            dic[name] = weight
        return dic
```

### 測資


```python
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
print("Dijkstra",g.Dijkstra(0))

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

print("Kruskal",g.Kruskal()) 
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}
    

參考網址:

https://www.w3schools.com/python/python_dictionaries.asp

https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

https://github.com/aaron1aaron2/my-learning-note

https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
