def get_arms(N: int, T: int) -> int:
    period = 4 * N - 2
    idx = (T - 1) % period

    if idx < 2 * N - 1:
        return 1 + idx
    else:
        return 4 * N - 1 - idx
N, T = map(int, input().split())
print(get_arms(N, T))