# 여러개의 변수를 동시에 초기화
a,b,c = 1,2,3
print(a)
print(b)
print(c)

# 예제 2 ~ 5 풀기
x = 10
print(x)

x,y,z=1,2,3
print(x, y, z)

x,y,z = 1, 1.111, "1"
print(type(x),type(y),type(z))

a = input('a: ')
b = input('b: ')
a, b = b, a
print("a: " + a)
print("b: " + b)