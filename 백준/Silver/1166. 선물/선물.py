def max_cube_size(N, L, W, H):
    l, r = 0, min(L, W, H)

    for _ in range(100):
        mid = (l + r) / 2
        count = int(L / mid) * int(W / mid) * int(H / mid)

        if count >= N:
            l = mid
        else:
            r = mid

    return l

N, L, W, H = map(int, input().split())
print(f"{max_cube_size(N, L, W, H):.9f}")