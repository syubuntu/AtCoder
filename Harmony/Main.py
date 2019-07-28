a = input()
b = int(a.split(' ')[1])
a = int(a.split(' ')[0])
l = a + b
if l % 2 == 1:
  print ('IMPOSSIBLE')
else:
  l = l / 2
  print(int(l))

