
# MergeSort文字說明、流程圖及比較

mergesort需要經過分割-->排序解決-->合併的步驟
一開始需要將list分割兩半，於是我先假設已經分好了arr1,arr2，設立p,q作為兩個arr的index，並設立空list:sort[]裝排序好的值。
先以自己的想法試試看merge(排序解決和合併)的部分~


```python
def merge(arr1,arr2):
    p = 0
    q = 0  #兩個arr的index
    sort = []
    a = len(arr1)+len(arr2)
    for i in range(a):
        if arr1[p] and arr2[q]: #把較小的append進sort[]
            if arr1[p] < arr2[q]:
                sort.append(arr1[p])
                p = p+1
            else:
                sort.append(arr2[q])
                q = q+1
                
    print(sort)
merge([5,3,9,1],[2,0,4,8])  #試看看
```

    [2]
    


```python
邏輯還不太完整，試著補缺完善~
改用while迴圈
添加arr到底的條件式
```


```python
def merge(arr1,arr2):
    p = 0
    q = 0  #兩個arr的index
    sort = []
     
        
    while p<len(arr1) and q<len(arr2):
        if arr1[p] <= arr2[q]: #把較小的append進sort[]
            sort.append(arr1[p])
            p = p+1
            
        else:
            sort.append(arr2[q])
            q = q+1
        
    while p == len(arr1) and q<len(arr2):  #當arr1到底
        sort.append(arr2[q])
        q = q+1
    while  q ==len(arr2) and p<len(arr1):  ##當arr2到底
        sort.append(arr1[p])
        p = p+1    
       
    print(sort)    
merge([5,1,3,4],[2,-5,-9])  #試看看  
```

    [2, -5, -9, 5, 1, 3, 4]
    

建立mergesort，分割輸入的list~
arr1取0到mid-1個，arr2取mid到最後一個


```python
def mergesort(arr):
    if len(arr) < 2:  #長度小於2，直接return
        return arr
    mid = len(arr)//2
    arr1 = mergesort(arr[:mid])  #前半段
    arr2 = mergesort(arr[mid:])  #後半段
    return merge(arr1,arr2)
```


```python
c = [-2, 0, 5, 5, 19, -6, 6, 3, 7, 9, 16, 11, 0, -6, -9, 6, 3]
mergesort(c)
```

    [-2, 0]
    [5, 5]
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-188-37dea29332c9> in <module>
          1 c = [-2, 0, 5, 5, 19, -6, 6, 3, 7, 9, 16, 11, 0, -6, -9, 6, 3]
    ----> 2 mergesort(c)
    

    <ipython-input-187-a95b34679584> in mergesort(arr)
          3         return arr
          4     mid = len(arr)//2
    ----> 5     arr1 = mergesort(arr[:mid])  #前半段
          6     arr2 = mergesort(arr[mid:])  #後半段
          7     return merge(arr1,arr2)
    

    <ipython-input-187-a95b34679584> in mergesort(arr)
          3         return arr
          4     mid = len(arr)//2
    ----> 5     arr1 = mergesort(arr[:mid])  #前半段
          6     arr2 = mergesort(arr[mid:])  #後半段
          7     return merge(arr1,arr2)
    

    <ipython-input-187-a95b34679584> in mergesort(arr)
          5     arr1 = mergesort(arr[:mid])  #前半段
          6     arr2 = mergesort(arr[mid:])  #後半段
    ----> 7     return merge(arr1,arr2)
    

    <ipython-input-186-0538af73c74c> in merge(arr1, arr2)
          5 
          6 
    ----> 7     while p<len(arr1) and q<len(arr2):
          8         if arr1[p] <= arr2[q]: #把較小的append進sort[]
          9             sort.append(arr1[p])
    

    TypeError: object of type 'NoneType' has no len()


這種寫法導致最後沒有值，len()會出錯。
試著把len()寫法換掉，精簡程式碼。
用+=代替append寫法。


```python
def merge(arr1,arr2):
    p = 0
    q = 0  #兩個arr的index
    sort = []
     
        
    while p<len(arr1) and q<len(arr2):  #還沒走訪到結尾
        if arr1[p] <= arr2[q]:   #把較小的append進sort[]
            sort.append(arr1[p])
            p = p+1
            
        else:
            sort.append(arr2[q])
            q = q+1
        
    sort += arr1[p:]  #若arr1有多，補上p之後的
    sort += arr2[q:]  #若arr2有多，補上q之後的
    return sort
```


```python
def mergesort(arr):
    if len(arr) < 2:
        return arr  #長度小於2，直接return
    mid = len(arr)//2
    arr1 = mergesort(arr[:mid])  #前半段
    arr2 = mergesort(arr[mid:])  #後半段
    return merge(arr1,arr2)
```


```python
##多加一些測值
list = [-2, 0, 5, 5, 19, -6, 6, 3, 7, 9, 16, 11, 0, -6, -9, 6, 3]
mergesort(list)
```




    [-9, -6, -6, -2, 0, 0, 3, 3, 5, 5, 6, 6, 7, 9, 11, 16, 19]




```python
與HeapSort比較:
    MergeSort的時間複雜度為O(n(logn))
    MergeSort的時間複雜度為O(n)
    穩定度較佳(stable)，較不會因為初始排序的不同影響運行效率。
```

參考資料:
    https://kopu.chat/2017/08/10/%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F-merge-sort/
    https://youtu.be/EeQ8pwjQxTM
    https://en.wikipedia.org/wiki/Merge_sort
