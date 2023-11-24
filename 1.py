# 1 : 1~10까지 숫자 중에서 홀수만 출력하는 코드 작성

for i in range(1, 11):
    if i % 2 != 0:
        print(i, end=' ')
        
        
# 2 : 리스트 a = [1, 2, 3, 4, 5]에 있는 모든 요소에 10을 곱한 후
# 새로운 리스트 b에 저장하는 코드 작성

a = [1, 2, 3, 4, 5]

for i in a:
    b = i * 10
    print(b, end=' ')


# 3 : 문자열 s = "Hello World"에 있는 모든 알파벳을 대문자로 바꾸는 코드를 작성

s = "Hello World"
print(s.upper())


# 4 : range(1, 101)로 생성된 숫자 중 3의 배수이면서 5의 배수인 숫자만 출력하는 코드 작성

for i in range(min(1, 101), (1*101) + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')

for i in range(1, 101):
    if i % 15 == 0:
        print(i, end=' ')
       
        
# 5 : 리스트 c = [10, 20, 30, 40, 50]를 역순으로 리스트 d에 저장

c = [10, 20, 30, 40, 50]

d = c.reverse()
print(c)


# 6 : 문자열 t = "This is a test"에 있는 모든 단어의 첫 글자만 출력하는 코드를 작성

t = "This is a test"
a = t.split(" ")

for i in a:
    print(i[0], end=' ')
    
    
# 7 : 리스트 f = [1, 2, 3, 4, 5]와 리스트 g = [6, 7, 8, 9, 10]을 합쳐서 (ex, 1+6, 2+7, ...)
# 리스트 h에 저장하기

f = [1, 2, 3, 4, 5]
g = [6, 7, 8, 9, 10]

# 방법 1 (검색)
n = [i+j for i, j in zip(f, g)]
print(n)

# 방법 2 (검색)
n = [f[i] + g[i] for i in range(len(f))]
print(n)


# 8 : 문자열 u = "Bing is awesome"에 있는 모든 모음(a, e, i, o ,u)의 개수를 세는 코드를 작성
# 검색
u = "Bing is awesome"
l = "a", "e", "i", "o" ,"u"
n = 0
for i in u:
    if i in l:
        n += 1
print(n)