
x=int(input('enter How many numbers:'))
count=0
list=[]

while count <x:
    count=count+1
    n=float( input('enter your number:'))
    list.append(n)

for i in range (x-1):

    if list[i]> list[i+1]:
        print('list is not sort')
        break
    if i==x-2:
        print('list is sort')