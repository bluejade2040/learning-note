
# HeapSort文字說明、流程圖及比較

Heapsort藉由最大值上升到tree的頂點，然後移除到list最後一項來完成排序。
heapsort()：將root為最大值的tree轉換成「由小到大」排好序的矩陣。把root丟到矩陣最後。
buildheap()：對所有子結點進行heapify()。
heapify()：「由上而下」，逐一檢查每個子根項，把最大值lar擺進子root。


```python
def heapsort(list): #提出最大值到最後一項
    buildheap(list)
    for i in range(2,n):
        list[0],list[i] = list[i],list[0] #最大值提出
        n = n-1  #n變成目前還沒被提出的數字個數
        heapify(list,lar,n)
        
def buildheap(list):
    n = len(list)
    for i in range(n//2): #n//2表示需要處理的root數量
        heapify(list,i,n)
def heapify(list,i,n): #建立最大值 
    
    left = i*2+1
    right = i*2+2
    
    if left <= n and list[left] > list[i]:
        lar = left
    else:
        lar = i
    if right <= n and list[right] > list[lar]:
        lar = right
    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  
        list[i],list[lar] = list[lar],list[i]
        heapify(list,lar,n)  #有替換就要再跑一次
```


```python
list = [5,3,8,1,9,0,8,11,13,6,7,10]
heapsort(list)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-24-c154f7465454> in <module>
          1 list = [5,3,8,1,9,0,8,11,13,6,7,10]
    ----> 2 heapsort(list)
    

    <ipython-input-23-04bc16e9a467> in heapsort(list)
          1 def heapsort(list): #提出最大值到最後一項
    ----> 2     buildheap(list)
          3     for i in range(2,n):
          4         list[0],list[i] = list[i],list[0] #最大值提出
          5         n = n-1  #n變成目前還沒被提出的數字個數
    

    <ipython-input-23-04bc16e9a467> in buildheap(list)
          9     n = len(list)
         10     for i in range(n//2): #n//2表示需要處理的root數量
    ---> 11         heapify(list,i,n)
         12 def heapify(list,i,n): #建立最大值
         13 
    

    <ipython-input-23-04bc16e9a467> in heapify(list, i, n)
         19     else:
         20         lar = i
    ---> 21     if right <= n and list[right] > list[lar]:
         22         lar = right
         23     if lar != i:  #判斷子根項是否最大，不是最大就替換掉
    

    IndexError: list index out of range


微調一下迴圈次數~


```python
def heapsort(list): #提出最大值到最後一項
    buildheap(list)
    for i in range(n):
        list[0],list[i] = list[i],list[0] #最大值提出
        n = n-1  #n變成目前還沒被提出的數字個數
        heapify(list,lar,n)
        
def buildheap(list):
    n = len(list)
    for i in range(n//2): #n//2表示需要處理的root數量
        heapify(list,i,n)
def heapify(list,i,n): #建立最大值 
    
    left = i*2+1
    right = i*2
    
    if left <= n and list[left] > list[i]:
        lar = left
    else:
        lar = i
    if right <= n and list[right] > list[lar]:
        lar = right
    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  
        list[i],list[lar] = list[lar],list[i]
        heapify(list,lar,n)  #有替換就要再跑一次     
```


```python
list = [5,3,8,1,9,0,8,11,13,6,7,10]
heapsort(list)
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-45-c154f7465454> in <module>
          1 list = [5,3,8,1,9,0,8,11,13,6,7,10]
    ----> 2 heapsort(list)
    

    <ipython-input-44-175d19495853> in heapsort(list)
          1 def heapsort(list): #提出最大值到最後一項
          2     buildheap(list)
    ----> 3     for i in range(n):
          4         list[0],list[i] = list[i],list[0] #最大值提出
          5         n = n-1  #n變成目前還沒被提出的數字個數
    

    UnboundLocalError: local variable 'n' referenced before assignment


UnboundLocalError: local variable 'n' referenced before assignment
表示內外層有相同的variable但不同的賦值所以出錯。
修改明確一點~


```python
def heapsort(list): #提出最大值到最後一項
    buildheap(list)
    n = len(list)
    for i in range(len(list)):
        list[0],list[i] = list[i],list[0] #最大值提出
        n = n-1  #n變成目前還沒被提出的數字個數
        heapify(list,n,i)
        
def buildheap(list):
    n = len(list)
    for i in range(n//2): #n//2表示需要處理的root數量
        heapify(list,i,n)  #創造出最大值在root的heap
        
def heapify(list,i,n): #建立子root為最大值 
    
    left = i*2+1
    right = i*2
    
    if left < n and list[left] > list[i]:
        lar = left
    else:
        lar = i
    if right < n and list[right] > list[lar]:
        lar = right
    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  
        list[i],list[lar] = list[lar],list[i]
        heapify(list,lar,n)  #有替換就要再跑一次
```


```python
for i in range(13//2): ##實驗一下for迴圈~
    print(1)
```

    1
    1
    1
    1
    1
    1
    


```python
list = [5,3,8,1,9,0,8,6,7,10]
heapsort(list)
print(list)
```

    [10, 9, 8, 5, 8, 3, 0, 1, 6, 7]
    


```python
在for迴圈的地方邏輯次數有錯，再換個寫法試試。
明確訂定開始值、結束值跟公差。
```


```python
def heapsort(list): #提出最大值到最後一項
    buildheap(list)
    n = len(list)
    for i in range(n-1,0,-1):
        list[0],list[i] = list[i],list[0] #最大值提出
        heapify(list,0,i)
        
def buildheap(list):
    n = len(list)
    for i in range(n,-1,-1):  #i從n到-1，每跑一次-1
        heapify(list,i,n)  #創造出最大值在root的heap
        
def heapify(list,i,n): #建立子root為最大值 
    
    left = i*2+1
    right = i*2
    
    if left < n and list[left] > list[i]:
        lar = left
    else:
        lar = i
    if right < n and list[right] > list[lar]:
        lar = right
    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  
        list[i],list[lar] = list[lar],list[i]
        heapify(list,lar,n)  #有替換就要再跑一次
```


```python
list = [3,1,0,8,6,7,10,15,9,13,18,14]
heapsort(list)
print(list)
```

    [0, 1, 3, 6, 7, 8, 9, 10, 13, 14, 15, 18]
    
流程圖:
![](https://github.com/bluejade2040/learning-note/blob/master/heapsort.jpg)


與MergeSort比較:
    HeapSort的時間複雜度為O(n(logn))
    HeapSort的時間複雜度為O(1)
    穩定度較差(unstable)，會因為初始排序的不同影響運行效率。

參考資料:
    https://www.cc.gatech.edu/classes/cs3158_98_fall/heapsort.html
    https://stackoverflow.com/questions/43700267/max-heapify-pseudocode
    https://youtu.be/MtQL_ll5KhQ
