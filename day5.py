#largest continuos sum 
def biggest_cont_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum =current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
    print(max_sum)
    return max_sum
biggest_cont_sum([1,2,-1,3,4,10,10,-10,-1])

##senetence reversal 
##basic algorithm of reversing the senetence is 

def manual_sentence(str):
    words = []
    spaces = [' ']
    length = len(str)
    i = 0
    while i < length:
        if str[i] not in spaces:
            word_start = i

            while i < length and str[i] not in spaces:
                i +=1
            words.append(str[word_start:i])
        i+= 1
    print(words)
    print( " ".join(reversed(words)))
    return " ".join(reversed(words))

manual_sentence("Iam a bastard")

## this is the optimised code which is having time complexity 
def sene_reversal(str):
    return " ".join(reversed(str.split()))
sene_reversal("Hai ra puka")


def colon_reversal(str):
    return " ".join(str.split()[::-1])
colon_reversal("iam hawlw")

##string compression ex: AAABBCCCD compres to A3B2C3D

def compression(str):
    #AAABBCCCDDE = A3B2C3D2E
    



    ##harry chapter2 variables and practice sheet done 
    #Data types : Integers ,floating point,string, booolean,none
    print(str(31)) # converting Integer to string 

#strings manipulations 
name = "Laxman is good"
greet = "boy"
c = name + greet
print(c)
print(name[0:6]) # same as name[:6]
print(name[0:])  # same as name[0:]
print(name[-4:-1]) # start stop step is the moto of this 
print(name[0::3],"This is using ::")
print(name[:0:-1],"This is used to reverse the string") 
story = "Once upon a time lo ,girlfriend girlfriend "
print(len(story))
print(story.endswith("gilrfriend"))
print(story.capitalize())
print(story.replace("once ","hai"))

##taknig inputs 
name  = input("Enter your name\n")
print("GOod monring"+ name)

stri = "This is  one  and only one string"
doublespace = stri.find("  ")
print(doublespace)

letter = ''' Dear <|NAME|>,
Greetings from coding houses .Iam happy to tell you that 
you are fucker !
Have a great day in your ahead! 
Date: <|DATE|> '''

name = input("Enter your name\n")
date = input("enter date\n" )
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)

def sing_space(stro):
    
    stro.replace(""," ")
    print(stro)
stro = "one of the line is single spaced"
sing_space(stro)

#different types of strings 
# 'laxman'  
# "laxman"
# ''' laxman'''
# string slicing 
name = "Laxman" # 0   1  2   3   4  5
print(len(name))#-5  -5  -4  -3 -2   -1
