L1=['_','_','_']
L2=['_','_','_']
L3=['_','_','_']
i=9
print(L1[0],L1[1],L1[2],sep='|')
print(L2[0],L2[1],L2[2],sep='|')
print(L3[0],L3[1],L3[2],sep='|')
while i>0:
    if i%2!=0:
        print("PLAYER 1 turn(X):")
        ch='X'
    else:
        print("PLAYER 2 turn(0):")
        ch='0'
    row=int(input("Enter row: "))
    col=int(input("Enter column: "))
    if row==1 :
          if L1[col-1]=='_':
            L1[col-1]=ch
          else:
            print("Wrong Input")
            print("Please re-enter")
            i+=1
    if row==2 :
          if L2[col-1]=='_':
            L2[col-1]=ch
          else:
            print("Wrong Input")
            print("Please re-enter")
            i+=1
    if row==3 :
          if L3[col-1]=='_':
            L3[col-1]=ch
          else:
            print("Wrong Input")
            print("Please re-enter")
            i+=1
        
    print(L1[0],L1[1],L1[2],sep='|')
    print(L2[0],L2[1],L2[2],sep='|')
    print(L3[0],L3[1],L3[2],sep='|')
    print()
    if L1==['X','X','X'] or L2==['X','X','X'] or L3==['X','X','X'] or \
           (L1[col-1]==L2[col-1]==L3[col-1]=='X') or\
           (L1[0]==L2[1]==L3[2]=='X') or (L1[2]==L2[1]==L3[0]=='X'):
        print('Player 1 winner')
        break
    if L1==['O','O','O'] or L2==['O','O','O'] or L3==['O','O','O'] or \
           (L1[col-1]==L2[col-1]==L3[col-1]=='O') or\
           (L1[0]==L2[1]==L3[2]=='O') or (L1[2]==L2[1]==L3[0]=='O'):
        print('Player 2 winner')
        break 
    i-=1
if i==0:
    print("DRAW")
 
