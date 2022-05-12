import random

n= int (input('how many number?'))

list=[]

for i in range (n) :
    x=random.randrange(1,100)
    list.append(x)
print(list)    