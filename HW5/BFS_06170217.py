#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict 
class Graph:
    
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.stack = []
        self.outcome = []
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
        outcome = [] 
        set = []  
        set.append(s)  
        confirm = [False] * (len(self.graph))
        confirm[s] = True   
        while set:
            s = set.pop(0)  
            outcome.append(s)
            for i in self.graph[s]: 
                if confirm[i] == False:
                    set.append(i)  
                    confirm[i] = True 
        return outcome
    def DFS(self, s):
        self.stack.append(s)
        confirm = [False] * (len(self.graph))
        confirm[s] = True 
        while self.stack:
            s = self.stack.pop() 
            self.outcome.append(s)
            for i in self.graph[s]:
                if confirm[i] == False:
                    self.stack.append(i)  
                    confirm[i] = True  
        return self.outcome

