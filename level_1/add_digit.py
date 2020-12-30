n =123
answer =0
ten = pow(10,len(str(n))-1)
print(ten)
print(n//ten)

while n>0:
    answer+= n//ten
    n = n -ten*(n//ten)
    ten  = ten/10
print(int(answer))