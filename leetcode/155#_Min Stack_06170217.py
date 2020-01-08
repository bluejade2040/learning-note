#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node: 
      
    def __init__(self,data): 
        self.data = data 
        self.next = None
        
class Stack: 
       
    def __init__(self): 
        self.head = None
        
  #檢查是否為空      
    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
      
  #加節點
    def push(self,data): 
          
        if self.head == None: 
            self.head = Node(data) 
              
        else: 
            newnode = Node(data) 
            newnode.next = self.head 
            self.head = newnode 
      
    #  抽最上層資料出來
    def pop(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            # Removes the head node and makes  
            #the preceeding one the new head 
            poppednode = self.head 
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data 
      
    # Return第一個值 
    def top(self): 
          
        if self.isempty(): 
            return None
              
        else: 
            return self.head.data 
      
    # Prints out the stack      
    def display(self): 
          
        iternode = self.head 
        if self.isempty(): 
            print("Stack Underflow") 
          
        else: 
              
            while(iternode != None): 
                  
                print(iternode.data,"->",end = " ") 
                iternode = iternode.next
            return

