n = int(input())
t = input()
p = []
for k in range(0,n,1):
  p.append(int(t.split(' ')[k]))
c = 0
for k in range(0,n,1):
  if p[k] == k+1:
    c += 1
if c == n - 2 or c == n:
  print('YES')
else:
  print('NO')

