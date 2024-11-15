n,x,y=map(int, input().split())
z=n*x
if y<=z and (z-y)%x==0:
    print("YES")
else:
    print("NO")
