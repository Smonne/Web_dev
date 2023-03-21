N = int(input())

a = list(map(int, input().split()))

for i in range(0, N, 2):

   print(a[i], end=" ")