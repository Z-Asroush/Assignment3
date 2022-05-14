import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

i = random.randint(0, len(words)-1)
word = words[i]
ans=[]
word = random.choice(words)
joon = 5

while  joon > 0  : 
    print('- ' * len(word))

    user_character = input('enter your letter:')
    user_character=(user_character. lower())
    
    if user_character in word:
        
        ans.append(user_character)
        print(ans)
        if len(ans)== len(word):
            break
        
        
    else:
        joon = joon - 1
        print('no')
