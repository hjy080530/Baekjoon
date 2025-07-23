import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        
        sejun = list(map(int, data[idx:idx + N]))
        idx += N
        sebi = list(map(int, data[idx:idx + M]))
        idx += M

        max_sejun = max(sejun)
        max_sebi = max(sebi)

        if max_sejun > max_sebi:
            results.append("S")
        elif max_sejun < max_sebi:
            results.append("B")
        else:
            results.append("S")  
    print("\n".join(results))

solve()