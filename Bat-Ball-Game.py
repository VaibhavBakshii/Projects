print('INSTRUCTIONS:')
print('There are two levels- First level you can score between 0 and 6 and second level between 3 and 6')
print('if the cpu guesses your no. youre out and vice versa')

s=0
m=0
u=0
s1=0
print('LEVEL 1')
print('Batting:')
while m<=10:
    n=int(input('enter no between 0 and 6'))
    import random
    c=random.randint(0,6)
    if c==n:
        print('out,score:',s)
        m+=1
        break
    else:
        s+=n
        m+=1
        print('score:',s)
print('Bowling:')
while u<=10:
    x=int(input('enter no between 0 and 6'))
    import random
    c1=random.randint(0,6)
    if c1==x:
        print('out! score of cpu:',s1)
        break
    else:
        s1+=c1
        print('score of cpu:',s1)
        u+=1
    if s1>s:
        break
if s1>s:
    print('CPU won!')
else:
    print('congrats you won!')
if s>s1:
    print('Level 2')
    print('Batting:')
    m=0
    s=0
    u=0
    s1=0
    while m<=10:
        n=int(input('enter no between 3 and 6'))
        import random
        c=random.randint(3,6)
        if c==n:
            print('out,score:',s)
            m+=1
            break
        else:
            s+=n
            m+=1
            print('score:',s)
    print('Bowling:')
    while u<=10:
        x=int(input('enter no between 3 and 6'))
        import random
        c1=random.randint(3,6)
        if c1==x:
            print('out! score of cpu:',s1)
            break
        else:
            s1+=c1
            print('score of cpu:',s1)
            u+=1
        if s1>s:
            break
if s1>s:
    print('CPU won!')
else:
    print('congrats you won!')
