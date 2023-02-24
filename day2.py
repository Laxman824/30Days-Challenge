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


 a =input("ent")