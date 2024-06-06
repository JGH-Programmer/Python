K = int(input())

List = []

for i in range(K):
    word = input()
    List.append((word,len(word)))

List = set(List)
List = sorted(List, key = lambda x : x[1])

for i in List:
    print(i[0])













