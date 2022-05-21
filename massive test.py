from tracemalloc import stop


a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
print('массив')
for i in range(len(a)):
    print(a[i])
a.sort()
print('отсортированный массив')
for i in range(len(a)):
    print(a[i])
stop