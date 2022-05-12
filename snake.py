
L= int(input('length of snake?'))

for i in range (L) :
    if i % 2 != 0:
        print ('#' ,end= '')
    else:
        print('*', end='')

