print("Hello world")

#Different types of time complexities (Big O )
#   O(1) Constant 
#   O(n)  Linear time : def linear
# O(n^2)  Quadratic time 

def comp(lst):
    # print(lst[0])
    midpoint = len(lst) //2
    for val in lst[:]:
        return 
        # print(val)
lst = [1,2,43,4]
comp(lst)

#worst case vs best case
def ucase(lst,target):
    for item in lst:
        if item == target:
            
            True
    
    return False
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ucase(lst,1) # best case as iin the first comparision we got element(O(1))
ucase (lst,22)#worst case ,no match still check every element O(n)
print(lst)

#Space complexity 
def printer(n):
    for x in range(n):
        print("hello ")
printer(10)#Hre only printing variable once i.e.O(1) and O(n) iteration(time cmplexity)

def creat_list(n):
    new = []
    for val in range(n):
        new.append("new_ele")
    return new
print(creat_list(4)) # here O(n) time and space cmplexity

#Dictonaries in python are an implementation of hash table.they have 
# key and value ex: d = {'a' : 1,'b':2}

import os
print(os.listdir())
# Harry chap 1 ################################################
print("Twinkle twinkle little star \n how are wonder what you are")

#REPL(Read eval Print LOOP)

def table(n):
    for i in range(1,10):#start,stop,step
        print(n," x",i, " =" ,(n*i) )
table(5)

import numpy as laxman
in_1 = laxman.array([[1,2,3],[3,2,1]])#here laxman is numpy library
in_2 = laxman.array([[4,5,6],[6,5,4]])
print("The input arrays are :",in_1,in_2)
out_arr = laxman.add(in_1,in_2)#add is operation we can do other operations also
print("The output of the operation perfromed above is: \n",out_arr)

import os
dir_path = "/home/laxman/Downloads/" 
for item in os.listdir(dir_path): 
    print(item)