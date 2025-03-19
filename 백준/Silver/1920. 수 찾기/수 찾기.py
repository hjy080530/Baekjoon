import sys

def main():
    N = int(sys.stdin.readline().strip())
    A = set(map(int, sys.stdin.readline().split()))
    
    M = int(sys.stdin.readline().strip())
    X = map(int, sys.stdin.readline().split())
    
    result = [1 if x in A else 0 for x in X]
    sys.stdout.write("\n".join(map(str, result)) + "\n")

main()