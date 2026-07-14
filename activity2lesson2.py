def palindrone(r):
    e = len(r) -1
    s = 0

    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
        return True
    
r = (1,2,3,3,2,1,)

if(palindrone(r)):
        print("Its a palindrone")
else:
        print("its not a palindrone")

