def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

N, M = map(int, input().split())
truth = list(map(int, input().split()))
truth_people = truth[1:]  
parties = []

parent = [i for i in range(N + 1)]

for _ in range(M):
    party = list(map(int, input().split()))
    people = party[1:]
    parties.append(people)
    for i in range(len(people) - 1):
        union(people[i], people[i + 1])

truth_roots = set(find(person) for person in truth_people)

cnt = 0
for party in parties:
    if all(find(p) not in truth_roots for p in party):
        cnt += 1

print(cnt)