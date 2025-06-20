import math

def is_triangle(x):
    d = 1 + 8 * x
    sqrt_d = int(math.isqrt(d))
    if sqrt_d * sqrt_d != d:
        return False
    n = (-1 + sqrt_d) // 2
    return n * (n + 1) // 2 == x

def solve():
    case_num = 1
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break

        count = 0
        sa = int(math.isqrt(a)) + 1
        sb = int(math.isqrt(b - 1))
        for s in range(sa, sb + 1):
            total = s * s
            if a < total < b and is_triangle(total - 1):
                count += 1

        print(f"Case {case_num}: {count}")
        case_num += 1

solve()
