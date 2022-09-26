print("Введите кол-во символов и выражение через ENTER")
a=[]
n=int(input())
for i in range(n):
    a.append(str(input()))
b='print('
for i in a:
    b+=i

b+=')'
exec(b)
  

