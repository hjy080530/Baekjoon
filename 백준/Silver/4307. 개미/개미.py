import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    L, N = map(int, input().split())
    positions = [int(input()) for _ in range(N)]
    
    min_time = max(min(pos, L - pos) for pos in positions)
    max_time = max(max(pos, L - pos) for pos in positions)
    
    print(min_time, max_time)