#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_k = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
    def addEdge(self,u,v,w):
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
        result =[]
        i = 0
        e = 0
        self.graph_k =  sorted(self.graph_k,key=lambda item: item[2]) 
        parent = [] 
        rank = [] 
        dic = {}
        name = {}
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
        for u,v,weight  in result:
            name = ('{}-{}').format(u,v)
            dic[name] = weight
        return dic

