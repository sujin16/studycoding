def check_pair(p):
    stack =[]
    for str in p:
        if str =='(': stack.append(str)
        elif len(stack)>0: stack.pop()

    return len(stack) ==0

def make_pair(p):
    u=''
    v=''
    for i in range(0,len(p),2):
        str = p[0:i+2]
        if str.count('(') ==str.count(')'):
            u=str
            v=p[i+2:]
            break
    if not check_pair(u): 
        u = u[1:-1]
        u =list(u)
        for i in range(len(u)):
            if u[i] ==')' :u[i] ='('
            elif u[i] =='(': u[i] =')'
        u ="".join(u)
        return '(' +make_pair(v) +  ')' + u
       
    if not check_pair(v): return u + make_pair(v)
    return u+v

def solution(p):
    if check_pair(p) : return p
    return make_pair(p)

p =')()()()('
print(solution(p))

