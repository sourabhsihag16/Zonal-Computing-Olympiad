''' question ref = https://www.iarcs.org.in/inoi/2014/zco2014/zco2014-1a.php '''
n,h=map(int,input().split())
st=list(map(int,input().split()))
op=list(map(int,input().split()))
k=0
le=len(op)
holding=False
for i in range(le):
    if op[i]==0:
        break
    elif op[i]==1 and k!=0: #Move left
        k=k-1
    elif op[i]==2 and  k!=n-1: #Move right
        k=k+1
    elif op[i]==3 and st[k]>0 and holding==False: #Pick up box
        st[k]=st[k]-1
        holding=True
    elif op[i]==4 and st[k]<h and holding==True:
        st[k]=st[k]+1
        holding=False
print(*st)
