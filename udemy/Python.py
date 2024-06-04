K = int(input())

List = []

for i in range(K):
    N,M = map(int,input().split())
    List.append((N,M))

List.sort()

for i in List:
    print(i[0], i[1])











