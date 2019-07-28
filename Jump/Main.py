x = input()
y = int(x.split(' ')[1])
x = int(x.split(' ')[0])

c = 0
k = [0,0]

while c <= 100000:
  if k[0] == x and k[1] == y:
    break
  elif k[0] < x:
    k[0] += 1
    k[1] += 2
  else:
    k[0] -= 1
    k[1] += 2
  c+=1
if c == 100001:
  c = -1
print(c)
