arr=["R","R","R","U","D","D"]
cur=[1,1]
i =0
n=5
while i<len(arr):
    add =cur.copy()
    if arr[i] =='R': add[1]+=1
    if arr[i] =='L': add[1]-=1
    if arr[i] =='U': add[0]-=1
    if arr[i] =='D': add[0]+=1
    if 1<=add[0]<=n and 1<=add[1]<=n:
        cur =add.copy()
    i+=1
print(cur)
    
