{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# HeapSort文字說明、流程圖及比較"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Heapsort藉由最大值上升到tree的頂點，然後移除到list最後一項來完成排序。\n",
    "heapsort()：將root為最大值的tree轉換成「由小到大」排好序的矩陣。把root丟到矩陣最後。\n",
    "buildheap()：對所有子結點進行heapify()。\n",
    "heapify()：「由上而下」，逐一檢查每個子根項，把最大值lar擺進子root。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heapsort(list): #提出最大值到最後一項\n",
    "    buildheap(list)\n",
    "    for i in range(2,n):\n",
    "        list[0],list[i] = list[i],list[0] #最大值提出\n",
    "        n = n-1  #n變成目前還沒被提出的數字個數\n",
    "        heapify(list,lar,n)\n",
    "        \n",
    "def buildheap(list):\n",
    "    n = len(list)\n",
    "    for i in range(n//2): #n//2表示需要處理的root數量\n",
    "        heapify(list,i,n)\n",
    "def heapify(list,i,n): #建立最大值 \n",
    "    \n",
    "    left = i*2+1\n",
    "    right = i*2+2\n",
    "    \n",
    "    if left <= n and list[left] > list[i]:\n",
    "        lar = left\n",
    "    else:\n",
    "        lar = i\n",
    "    if right <= n and list[right] > list[lar]:\n",
    "        lar = right\n",
    "    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  \n",
    "        list[i],list[lar] = list[lar],list[i]\n",
    "        heapify(list,lar,n)  #有替換就要再跑一次"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-c154f7465454>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlist\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m9\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m13\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mheapsort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-23-04bc16e9a467>\u001b[0m in \u001b[0;36mheapsort\u001b[1;34m(list)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mheapsort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;31m#提出最大值到最後一項\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[0mbuildheap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m         \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;31m#最大值提出\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m  \u001b[1;31m#n變成目前還沒被提出的數字個數\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-23-04bc16e9a467>\u001b[0m in \u001b[0;36mbuildheap\u001b[1;34m(list)\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m//\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;31m#n//2表示需要處理的root數量\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m         \u001b[0mheapify\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mheapify\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;31m#建立最大值\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-23-04bc16e9a467>\u001b[0m in \u001b[0;36mheapify\u001b[1;34m(list, i, n)\u001b[0m\n\u001b[0;32m     19\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m         \u001b[0mlar\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m     \u001b[1;32mif\u001b[0m \u001b[0mright\u001b[0m \u001b[1;33m<=\u001b[0m \u001b[0mn\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mright\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m>\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlar\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m         \u001b[0mlar\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mright\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mlar\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m:\u001b[0m  \u001b[1;31m#判斷子根項是否最大，不是最大就替換掉\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "list = [5,3,8,1,9,0,8,11,13,6,7,10]\n",
    "heapsort(list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "微調一下迴圈次數~"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heapsort(list): #提出最大值到最後一項\n",
    "    buildheap(list)\n",
    "    for i in range(n):\n",
    "        list[0],list[i] = list[i],list[0] #最大值提出\n",
    "        n = n-1  #n變成目前還沒被提出的數字個數\n",
    "        heapify(list,lar,n)\n",
    "        \n",
    "def buildheap(list):\n",
    "    n = len(list)\n",
    "    for i in range(n//2): #n//2表示需要處理的root數量\n",
    "        heapify(list,i,n)\n",
    "def heapify(list,i,n): #建立最大值 \n",
    "    \n",
    "    left = i*2+1\n",
    "    right = i*2\n",
    "    \n",
    "    if left <= n and list[left] > list[i]:\n",
    "        lar = left\n",
    "    else:\n",
    "        lar = i\n",
    "    if right <= n and list[right] > list[lar]:\n",
    "        lar = right\n",
    "    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  \n",
    "        list[i],list[lar] = list[lar],list[i]\n",
    "        heapify(list,lar,n)  #有替換就要再跑一次     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "ename": "UnboundLocalError",
     "evalue": "local variable 'n' referenced before assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnboundLocalError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-45-c154f7465454>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mlist\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m9\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m8\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m13\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mheapsort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-44-175d19495853>\u001b[0m in \u001b[0;36mheapsort\u001b[1;34m(list)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mheapsort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;31m#提出最大值到最後一項\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mbuildheap\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m         \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;31m#最大值提出\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m  \u001b[1;31m#n變成目前還沒被提出的數字個數\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mUnboundLocalError\u001b[0m: local variable 'n' referenced before assignment"
     ]
    }
   ],
   "source": [
    "list = [5,3,8,1,9,0,8,11,13,6,7,10]\n",
    "heapsort(list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "UnboundLocalError: local variable 'n' referenced before assignment\n",
    "表示內外層有相同的variable但不同的賦值所以出錯。\n",
    "修改明確一點~"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heapsort(list): #提出最大值到最後一項\n",
    "    buildheap(list)\n",
    "    n = len(list)\n",
    "    for i in range(len(list)):\n",
    "        list[0],list[i] = list[i],list[0] #最大值提出\n",
    "        n = n-1  #n變成目前還沒被提出的數字個數\n",
    "        heapify(list,n,i)\n",
    "        \n",
    "def buildheap(list):\n",
    "    n = len(list)\n",
    "    for i in range(n//2): #n//2表示需要處理的root數量\n",
    "        heapify(list,i,n)  #創造出最大值在root的heap\n",
    "        \n",
    "def heapify(list,i,n): #建立子root為最大值 \n",
    "    \n",
    "    left = i*2+1\n",
    "    right = i*2\n",
    "    \n",
    "    if left < n and list[left] > list[i]:\n",
    "        lar = left\n",
    "    else:\n",
    "        lar = i\n",
    "    if right < n and list[right] > list[lar]:\n",
    "        lar = right\n",
    "    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  \n",
    "        list[i],list[lar] = list[lar],list[i]\n",
    "        heapify(list,lar,n)  #有替換就要再跑一次"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "for i in range(13//2): ##實驗一下for迴圈~\n",
    "    print(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 9, 8, 5, 8, 3, 0, 1, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "list = [5,3,8,1,9,0,8,6,7,10]\n",
    "heapsort(list)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "在for迴圈的地方邏輯次數有錯，再換個寫法試試。\n",
    "明確訂定開始值、結束值跟公差。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heapsort(list): #提出最大值到最後一項\n",
    "    buildheap(list)\n",
    "    n = len(list)\n",
    "    for i in range(n-1,0,-1):\n",
    "        list[0],list[i] = list[i],list[0] #最大值提出\n",
    "        heapify(list,0,i)\n",
    "        \n",
    "def buildheap(list):\n",
    "    n = len(list)\n",
    "    for i in range(n,-1,-1):  #i從n到-1，每跑一次-1\n",
    "        heapify(list,i,n)  #創造出最大值在root的heap\n",
    "        \n",
    "def heapify(list,i,n): #建立子root為最大值 \n",
    "    \n",
    "    left = i*2+1\n",
    "    right = i*2\n",
    "    \n",
    "    if left < n and list[left] > list[i]:\n",
    "        lar = left\n",
    "    else:\n",
    "        lar = i\n",
    "    if right < n and list[right] > list[lar]:\n",
    "        lar = right\n",
    "    if lar != i:  #判斷子根項是否最大，不是最大就替換掉  \n",
    "        list[i],list[lar] = list[lar],list[i]\n",
    "        heapify(list,lar,n)  #有替換就要再跑一次"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 3, 6, 7, 8, 9, 10, 13, 14, 15, 18]\n"
     ]
    }
   ],
   "source": [
    "list = [3,1,0,8,6,7,10,15,9,13,18,14]\n",
    "heapsort(list)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "與MergeSort比較:\n",
    "    HeapSort的時間複雜度為O(n(logn))\n",
    "    HeapSort的時間複雜度為O(1)\n",
    "    穩定度(stable)較差"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "參考資料:\n",
    "    https://www.cc.gatech.edu/classes/cs3158_98_fall/heapsort.html\n",
    "    https://stackoverflow.com/questions/43700267/max-heapify-pseudocode\n",
    "    https://youtu.be/MtQL_ll5KhQ"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
