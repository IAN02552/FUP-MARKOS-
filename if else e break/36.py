def funcao(x):  
    c = 1
    r = 1  
    div = 1
    while x >= c:    
        div = 0 
        for j in range(1,c+1):
            if c%j == 0:
                div += 1
        if div == 2 and x%c == 0:
            r = c
            x = x/c
        c += 1
    return r    
x = int(input(""))
y = funcao(x)
print(f"{y}")