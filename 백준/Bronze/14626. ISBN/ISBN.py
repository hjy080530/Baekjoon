isbn = input()

weights = [1, 3] * 6 
star_idx = isbn.index('*')

total = 0
for i in range(12):
    if i == star_idx:
        continue
    total += int(isbn[i]) * weights[i]

check_digit = int(isbn[12])

for x in range(10):
    temp_total = total + x * weights[star_idx]
    if (temp_total + check_digit) % 10 == 0:
        print(x)
        break