from datetime import date

def d_day(y1, m1, d1, y2, m2, d2):
    if (y2, m2, d2) >= (y1 + 1000, m1, d1):
        return "gg"
    
    start = date(y1, m1, d1)
    end = date(y2, m2, d2)
    return f"D-{(end - start).days}"

if __name__ == "__main__":
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    print(d_day(y1, m1, d1, y2, m2, d2))
