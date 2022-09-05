p=0
a=input('press enter to start')
print('Guess the name of the song!')
print('RULES: Enter songs in lower case')
print('ignore special characters')
print('type "use hint" to use hint')
print('max two hints allowed')
b=input('Ready?(y/n)')
hi=2
if b=='y':
    print('level 1, Here we go')
    print('song 1:')
    c=input('Lately I been, I been losing sleep,Dreaming about the things that we could be')
    if c=="counting stars":
        p+=10
        print('Great!')
        print('score so far',p)
    elif c=='use hint':
        c=input('Song by OneRepublic')
        if c=="counting stars":
            p+=10
            print('Great!')
            print('score so far',p)
        else:
            print('wrong! Next song...')
            print('score so far:',p)
            print('song name: counting stars')
        
        hi-=1
    else:
        print('wrong! Next song...')
        print('score so far:',p)
        print('song name: counting stars')
        
    print('song 2:')
    d=input('When you nod your head yes but you wanna say no')
    if d=='wdym' or d=='what do you mean':
        print('Great!')
        p+=10
        print('score so far',p)
    elif d=='use hint':
        d=input('Song by Justin Bieber from the album Purpose ')
        if d=='wdym' or d=='what do you mean':
            print('Great!')
            p+=10
            print('score so far',p)
        else: 
            print('wrong! Next song...')
            if p>0:
                p-=5
            print('score:',p)
            print('song name: what do you mean by Justin Bieber')  
        hi-=1    
    else:
        print('wrong! Next song...')
        if p>0:
            p-=5
        print('score:',p)
        print('song name: what do you mean by Justin Bieber')

    print('song 3:')
    d=input('Do you got plans tonight?')
    if d=='lost in japan':
        p+=10
        print('Great!')
        print('score so far',p)
        if p==30:
            print('you are killing it')
    elif d=='use hint':
        if hi>0:
            d=input('Song by Shawn Mendes')
            if d=='lost in japan':
                p+=10
                print('Great!')
                print('score so far',p)
                if p==30:
                        print('you are killing it')
            else: 
                print('wrong! Next song...')
                if p>0:
                    p-=5
                    print('score:',p)
                    print('song name: Lost in Japan ')  
                    hi-=1
        else:
             d=input('cant use more hints')
             if d=='lost in japan':
                 p+=10
                 print('Great!')
                 print('score so far',p)
            
    else:
        print('wrong! Next song...')
        if p>0:
            p-=5
        print('score so far:',p)
        print('song name: lost in japan by Shawn Mendes')
    print('song 4:')
    e=input('dancing in the dark, with you between my arms')
    if e=='perfect':
        print('Great!')
        p+=10
        print('score so far',p)
        if p==40:
            print('4/4 not bad!')
    elif e=='use hint':
        if hi>0:
            e=input('Song by Ed Sheeran')
            if e=='perfect':
                p+=10
                print('Great!')
                print('score so far',p)
                hi-=1
        else:
            e=input('cant use more hints')
            if e=='perfect':
                p+=10
                print('Great!')
                print('score so far',p)
            
    else:
        print('wrong! Next song...')
        if p>0:
            p-=5
        print('score so far:',p)
        print('song name: perfect by Ed Sheeran')
        if p==0:
            print('uh oh maybe you got this song')
    print('song 5:')
    f=input('oh oh sometimes, i get a good feeling, yeah')
    if f=='levels':
        p+=10
        print('correct!')
        print('score so far:',p)
    elif f=='use hint': 
        if hi>0:
            f=input('Song by Avicii')
            if f=='levels':
                p+=10
                print('Great!')
                print('score so far',p)
                hi-=1
        else:
            f=input('cant use more hints')
            if f=='levels':
                p+=10
                print('Great!')
                print('score so far',p)
            
    else:
        print('incorrect')
        if p>0:
            p-=5
        print('song name: levels by avicii')
        print('score so far:',p)
if p>=30:
    print("congrats! now level 2")
    print('song 6:')
    g=input("Climb on board , we'll go slow and high tempo")
    if g=='pillowtalk':
        p+=10
        print('correct!')
        print('score so far:',p)
    elif g=='use hint':
        if hi>0:
            g=input('Song by Zayn')
            if g=='pillowtalk':
                p+=10
                print('Great!')
                print('score so far',p)
                hi-=1
        else:
            g=input('cant use more hints')
            if g=='pillowtalk':
                p+=10
                print('Great!')
                print('score so far',p)
            
    else:
        print('incorrect')
        if p>0:
            p-=5
        print('song name: pillowtalk by zayn')
        print('score so far:',p)
    print('song 7:')
    h=input("look at you sideways party on tilt")
    if h=='sunflower':
        p+=10
        print('correct!')
        print('score so far:',p)
    elif h=='use hint':
        if hi>0:
            h=input('Song by Post Malone and Swae Lee from the movie Into the spiderverse')
            if h=='sunflower':
                p+=10
                print('Great!')
                print('score so far',p)
                hi-=1
        else:
            h=input('cant use more hints')
            if h=='sunflower':
                p+=10
                print('Great!')
                print('score so far',p)
            
    else:
        print('incorrect')
        if p>0:
            p-=5
        print('song name: sunflower by post malone')
        print('score so far:',p)
    print('song 8:')
    i=input("we dont love anymore, what was all of it for")
    if i=='we dont talk anymore':
        p+=10
        print('correct!')
        print('score so far:',p)
    elif i=='use hint':
        if hi>0:
            i=input('Song by Charlie Puth and Selena Gomez')
            if i=='we dont talk anymore':
                p+=10
                print('Great!')
                print('score so far',p)
                hi-=1
        else:
            i=input('cant use more hints')
            if i=='we dont talk anymore':
                p+=10
                print('Great!')
                print('score so far',p)
            
    else:
        print('incorrect')
        if p>0:
            p-=5
        print('song name: we dont talk anymore by charlie puth and selena gomez')
        print('score so far:',p)
    print('song 9:')
    j=input("I'll rent a beach house in Miami ,Wake up with no jammies ")
    if j=='thats what i like':
        p+=10
        print('correct!')
        print('score so far:',p)
    elif j=='use hint':
        if hi>0:
            j=input('Song by Bruno Mars')
            if j=='thats what i like':
                p+=10
                print('Great!')
                print('score so far',p)
                hi-=1
        else:
            j=input('cant use more hints')
            if j=='thats what i like':
                p+=10
                print('Great!')
                print('score so far',p)
            
    else:
        print('incorrect')
        if p>0:
            p-=5
        print('song name: thats what i like by Bruno Mars')
        print('score so far:',p)
    print('song 10:')
    k=input("I'm bulletproof nothing to lose ,Fire away, fire away")
    if k=='titanium':
        p+=10
        print('correct!')
        
    elif k=='use hint':
        if hi>0:
            k=input('Song by David Guetta and Sia')
            if k=='titanium':
                p+=10
                print('Great!')
                
                hi-=1
        else:
            k=input('cant use more hints')
            if k=='titanium':
                p+=10
                print('Great!')
                
            
    else:
        print('incorrect')
        if p>0:
            p-=5
        print('song name: Titanium by Sia')
        
    
    
    
    if p==100:
        print('holy moly you got all correct')
        print('final score:100')
    elif p>=80:
        print('total score:',p,'not bad at all')
    elif p>=60:
        print('total score:',p,'hmm decent')
    elif p>=30:
        print('total score:',p,"well... could've been worse")
    else:
        print('total score:',p,'you need to listen to more songs :P')
print('Thank you for playing!')
    
    
        
    
        
