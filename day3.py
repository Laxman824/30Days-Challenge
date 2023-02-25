#Array based sequences 
li = [1,2,3]
tu = (1,2,3)
str = '123'
dict = {"K":"2"}
print(dict["K"])

#dynamic array by using the builtin ctypes .

class M(object):
    def public(self):
        print("Iam public now")
    def private(self):
        print("Iam Private now!")
m = M()# initially callng class M() function
m.public() #sub functions are public and private are called
m.private()#sub funcs contains print stmts
###############################Dynamic array #####
import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capactiy = 1
        self.A = self.make_array(self.capactiy)
    def __len__(self): # returns size of array
    
        return self.n
    def __getitem__(self,k):# return element at index k 
        
        if not 0 <= k < self.n :
            return IndexError('K is out of bonds')
        return self.A[k] 
    
    def append(self,ele):
        #first  check if capacity/size is full
        if self.n == self.capactiy: 
            self._resize(2*self.capacity)
        self.A[self.n] = ele #just insert at the end of arr
        self.n += 1 
        
    def _resize(self,new_capacity):
        
        B = self.make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capactiy = new_capacity
    
    def make_array(self,new_capacity):
        return (new_capacity*ctypes.py_object)()
arr = DynamicArray()
print(arr.append(1))
len(arr)
print(type(arr))
print("The length of the arras is ",arr[0])


# a =input("ent")
##harry Chapter 2 practice set
def add_s():
    # a = int(input("enter the first input"))
    # b = int(input("enter the second input"))
    a= 9
    b = 9
    s= print("sum of both is",a+b)
    print(type(s))
add_s()

#typecast the data type

a = '123'
print(type(a))
a = int(a) #here just changed the datatype to int 
print(type(a))
print(2 + a) # tadaaa output is 125 :i.e 123 +2

#### 
def remainder():
    # p = input("ENter a number")
    p = 4
    q = 2
    p = int(p)
    print(type(p))
    print("The reminader for num div 2 is",p%q)
remainder()    
#comparisions done 
def compare():
    a = 34
    b = 80
    if (a > b):
        print("a is greater than b") 
    else :
        print("a is less than b")
compare()

##
def average():
    a = 8 
    b= 8
    # a = int(input("enter a number"))
    # b = int(input("enter a number"))
    print("the average is ",(a+b)//2)
average()

def square():
    # a = int(input("enter a number fr squareing "))
    a = 4
    print("the square of num is ",a*a)
square()
## harry chap2 practicse done
#anagram 
# def anagram():
#     a = "dog"
#     b = "god"
#     if len(a) == len(b):
#         print("yeah chances are there")
#         if a[i]== b[i]: #basically here checking if elemetns 
#             print("yes anagram")
#     else:
#         print("it is not anagram")
def anagram(string1,string2):
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower()
    # print(type(string1))
    # print(string2)
    if len(string1) != len(string2):
        False#base case for count 
    count = {}
    # print(type(count))

    for item in string1 :
        if item in count :
            # print(type(item))
            count[item] += 1
        else:
            count[item] = 1
    for item in string2: #if already in hash/dict above then reduce
        if item in count:
            count[item] -= 1
        else:
            count[item] =1
    for p in count:
        if  count[p] != 0:
            print("not a anagram")
            return False
    print("it is a anagram")
    return True
    
anagram('clint eastwood','old west action')
## this can be optimised by direcltly sorting the input 
def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    s= (sorted(s1) == sorted(s2))
    if s is True :
        print("it is anagram")
    else: 
        print("it is not ") #sort and compare if same True else false
anagram2('clint ','old west action')
##array pair sum

def pair_sum(arr,k):
    for i in range(len(arr)):
        if arr[i] + arr[i+1] == k:
            print("(",arr[i],",",arr[i+1],")")
            arr[i]+= 1 
            arr[i+1] += 1
            
            return arr[i],arr[i+1]
        else:
            arr[i]+= 1 
            arr[i+1] += 1
    
    return False
pair_sum([1,3,2,2],4)#here  it is not seeing the next set of elements not an
#accurate answer or wrong answer is producing

def pairsum(arr,k):
    seen = set()
    output = set()

    for num in arr: 
        target = k-num
        if target not in  seen:
            seen.add(num)
        else:
            output.add( (min(num,target),max(num,target)))
    print(output)
    return output
pairsum([1,3,2,2],4)

def arr_sequence(arr1,arr2):
    # sorted(arr1) == sorted(arr2)
    arr1.sort()
    arr2.sort()
    for num1,num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]
arr1 =[1,3,2,2]
arr2 = [1,3,2]
arr_sequence(arr1,arr2)
