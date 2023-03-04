#list
childhood_friends = ["ashish","payal","sachin"]
print(childhood_friends[:-1])
print(childhood_friends[0:3])

#declaration of tuple 
t = (1,2,3,4,5,1)
# t[0] =  8 #this cannot be updated in tuple since it is immutable
print(t[0])
print(t[0])
t = (1989,) # corret way to declare single element 
print(t)
#tuple methods 
t = (1,2,3,4,5,5,5,1,2,1)
print(t.count(1)) #this method gives the count of element 
print(t.index(3))
f1 = input("enter the name of 1")
f2 = input("enter the name of 2 ")


#students entering marks 
science = int(input("enter the marks"))
social  = int(input("enter the marks: "))

mymarks = [science,social]
mymarks.sort()
print(mymarks)

#chapter4 practice harry
#1 program to store svevn fruits in list given by user 
# fruit1 = input("enter furitname 1 ")
# fruit2 = input("enter fruitanme 2")
# fruit3 = input("enter fruitanme 2")
# fruit4 = input("enter fruitanme 2")
# fruit5 = input("enter fruitanme 2")

# allfruits = [fruit1,fruit2,fruit3,fruit4,fruit5]
# print(allfruits)
#22 program to accpet marks of 6 stundetns and sort it 
fruit1 = int(input("enter marks 1 "))
fruit2 = int(input("enter fruitanme 2"))
fruit3 = int(input("enter fruitanme 2"))
fruit4 = int(input("enter fruitanme 2"))
fruit5 = int(input("enter fruitanme 2"))

allmarks = [fruit1,fruit2,fruit3,fruit4,fruit5]
print(allmarks.sort) 
