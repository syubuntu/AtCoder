a =  input()
b = int(a.split(' ')[1])
a = int(a.split(' ')[0])
ans = a*b
if ans % 2 == 0:
    print('Even')
else:
    print('Odd')

