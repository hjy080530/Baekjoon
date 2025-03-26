def num_residents(k, n):
    apartment = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, n + 1):
        apartment[0][i] = i
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            apartment[floor][room] = apartment[floor][room - 1] + apartment[floor - 1][room]
    
    return apartment[k][n]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(num_residents(k, n))
