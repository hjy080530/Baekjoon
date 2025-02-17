A, B = map(int, input().split())
C = int(input())

tm = A * 60 + B + C 
nh = (tm//60) % 24
nm = tm% 60

print(nh,nm)