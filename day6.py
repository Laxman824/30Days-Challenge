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