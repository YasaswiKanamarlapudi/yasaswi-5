s=input()
q=int(input())
sub=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
ss=""
for i in range(q):
    d,p=input().split()
    d=d.upper()
    p=int(p)
    if d=='L':
        n=s[p:]
        ss=ss+n[0]
    else:
        n=s[:-p]
        ss=ss+n[0]
c=0
for i in sub:
    if(sorted(i)==sorted(ss)):
        c=1
        break
if c==1:
    print("YES")
else:
    print("NO")
        

        
        
        
