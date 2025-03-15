import sys  
input = sys.stdin.read  
data = input().splitlines()  

t = int(data[0])  
result = []  

for i in range(1, t + 1):  
    x1, y1, r1, x2, y2, r2 = map(int, data[i].split())  
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  
    
    if d == 0 and r1 == r2:  
        result.append(-1)  
    elif abs(r1 - r2) < d < (r1 + r2):  
        result.append(2)  
    elif d == (r1 + r2) or d == abs(r1 - r2):  
        result.append(1)  
    else:  
        result.append(0)  

sys.stdout.write("\n".join(map(str, result)) + "\n")  