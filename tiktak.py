# ( a1 b2 c3 )( d4 e5 f6 )( g7 h8 i9 )
# ( a1 d4 g7 )( b2 e5 h8 )( c3 f6 i9 )
# ( a1 e5 i9 )( g7 e5 c3 )

print("WElcome To Tik Tak Game")

list=[0]

a="-"
b="-"
c="-"
d="-"
e="-"
f="-"
g="-"
h="-"
i="-"

print("------Position----------")
print("1 2 3")
print("4 5 6")
print("7 8 9")


def pr():
    print("------Position----------")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")

    print("-------Game---------")
    print(a,b,c)
    print(d,e,f)
    print(g,h,i)


def putxo(location,p_id):
    global a,b,c,d,e,f,g,h,i

    if location==1:
        a=p_id
        pr()
    if location==2:
        b=p_id
        pr()
    if location==3:
        c=p_id
        pr()
    if location==4:
        d=p_id
        pr()
    if location==5:
        e=p_id
        pr()
    if location==6:
        f=p_id
        pr()
    if location==7:
        g=p_id
        pr()
    if location==8:
        h=p_id
        pr()
    if location==9:
        i=p_id
        pr()

def chk(p_id):
    global a,b,c,d,e,f,g,h,i
    # ( a1 b2 c3 )( d4 e5 f6 )( g7 h8 i9 )
    if a==p_id and b==p_id and c==p_id:
        return True
    if d==p_id and e==p_id and f==p_id:
        return True
    if g==p_id and h==p_id and i==p_id:
        return True
    # ( a1 d4 g7 )( b2 e5 h8 )( c3 f6 i9 )   
    if a==p_id and d==p_id and g==p_id:
        return True
    if b==p_id and e==p_id and h==p_id:
        return True
    if c==p_id and f==p_id and i==p_id:
        return True
    # ( a1 e5 i9 )( g7 e5 c3 )
    if a==p_id and e==p_id and i==p_id:
        return True
    if g==p_id and e==p_id and c==p_id:
        return True
    return False

count=1
while (count<10):
    count=count+1
    flag=0
          
    p1=int(input("\n Put X (1 to 9) : "))
    if(p1>9):
        print("Soory put bitwin 1 to 9")
        break
    # chak exist or not
    for q in list:
        if q==p1:
            print("Dont Cheet A game .. ");
            flag=1
            break
    
    if flag==1:
        break
    
    list.append(p1)
    putxo(p1,"X")
    ans=chk("X")
    if ans==True:
        print("\n Player X Winn \n")
        break

    # Player 2 
    p2=int(input("\n Put O (1 to 9) : "))
    if(p1>9):
        print("Soory put bitwin 1 to 9")
        break

    for q in list:
        if q==p2:
            print("Dont Cheet A game");
            flag=1
            break

    if flag==1:
        break
    
    list.append(p2)
    putxo(p2,"O")
    ans=chk("O")
    if ans==True:
        print("Player O Winn ")
        break
