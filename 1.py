## 문제 1 : 1~10까지 숫자 중에서 홀수만 출력하는 코드 작성

for i in range(1, 11):
    if i % 2 != 0:
        print(i, end=' ')
        
        
## 문제 2 : 리스트 a = [1, 2, 3, 4, 5]에 있는 모든 요소에 10을 곱한 후
## 새로운 리스트 b에 저장하는 코드 작성

a = [1, 2, 3, 4, 5]

for i in a:
    b = i * 10
    print(b, end=' ')


## 문제 3 : 문자열 s = "Hello World"에 있는 모든 알파벳을 대문자로 바꾸는 코드를 작성

# 문제 3 - 풀이 1 (upper 함수)
s = "Hello World"
print(s.upper())

# 문제 3 - 풀이 2
s = "Hello World"

for i in range(len(s)):
    result = s[i]
    
    if result == 'H':
        print('H', end='')
    elif result == 'e':
        print('E', end='')
    elif result == 'l':
        print('L', end='')
    elif result == 'o':
        print('O', end='')
    elif result == ' ':
        print(' ', end='')
    elif result == 'W':
        print('W', end='')
    elif result == 'r':
        print('R', end='')
    elif result == 'd':
        print('D', end='')

# 문제 3 - 풀이 3 (ASCII)
s = "Hello World"
for i in s:
    print(ord(i)) # 문자열 s를 for문으로 한 글자씩 출력하고, 아스키코드 10진수로 변환
    
    72 # "H"를 아스키코드로 변환한 값
    101
    108
    108
    111
    32
    87 # "W"를 아스키코드로 변환한 값
    111
    114
    108
    100
    
s = "Hello World"  # 위의 출력 결과와 아스키코드 표(검색)를 통해

for i in s:
    if ord(i) > 90:  # 대문자는 65~90 이고, 대문자(A)와 소문자(a)의 차이가 32 인 것을 알았음 
        result = ord(i) - 32  # i에 대입된 문자가 90보다 크면 소문자이므로 32를 빼서 대문자로 변환
        print(chr(result), end='')  # chr 함수로 다시 문자로 변환
    elif ord(i) < 90:
        result = ord(i)
        print(chr(result), end='')


## 문제 4 : range(1, 101)로 생성된 숫자 중 3의 배수이면서 5의 배수인 숫자만 출력하는 코드 작성

for i in range(1, 101):
    if i % 3 ==0 and i % 5 == 0:
        print(i, end=' ')

        
## 문제 5 : 리스트 c = [10, 20, 30, 40, 50]를 역순으로 리스트 d에 저장

c = [10, 20, 30, 40, 50]

result = c[::-1]
print(result)


## 문제 6 : 문자열 t = "This is a test"에 있는 모든 단어의 첫 글자만 출력하는 코드를 작성

# 문제 6 - 풀이 1 (split)
t = "This is a test"
a = t.split(" ")  # split를 사용하여 띄어쓰기를 기준으로 슬라이싱 ['This', 'is', 'a', 'test']

for i in a:
    print(i[0], end=' ')  # 인덱스를 사용하여 0번째에 오는 값들만 출력

# 문제 6 - 풀이 2
t = "This is a test"

for i in range(len(t)):
    first = t[i]
    
    if first == 'T':
        print(first, end=' ')
    elif first == 'i' and i % 5 == 0:
        print(first, end=' ')
    elif first == 'a' and i % 2 == 0:
        print(first, end=' ')
    elif first == 't' and i % 10 == 0:
        print(first, end=' ')

# 문제 6 - 풀이 3 (chat GPT 해석)
t = "This is a test"
word_start = True

for char in t:
    if char == ' ' or char in [',', '.', '!', '?', ';', ':', '"', "'"]:
        word_start = True
    elif word_start:
        print(char, end=' ')
        word_start = False


## 문제 7 : 리스트 f = [1, 2, 3, 4, 5]와 리스트 g = [6, 7, 8, 9, 10]을 합쳐서
## 리스트 h에 저장하기 (ex, 1+6, 2+7, ...)

# 문제 7 - 풀이 1
f = [1, 2, 3, 4, 5]
g = [6, 7, 8, 9, 10]

for i in range(len(f)):
    for j in range(len(g)):
        if i == j:
            print(f[i] + g[j], end=' ')
            
 # 문제 7 - 풀이 2 (인터넷 검색)         
f = [1, 2, 3, 4, 5]
g = [6, 7, 8, 9, 10]

n = [i+j for i, j in zip(f, g)]
print(n)

 # 문제 7 - 풀이 3 (인터넷 검색)         
f = [1, 2, 3, 4, 5]
g = [6, 7, 8, 9, 10]

n = [f[i] + g[i] for i in range(len(f))]
print(n)


## 문제 8 : 문자열 u = "Bing is awesome"에 있는 모든 모음(a, e, i, o ,u)의 개수를 세는 코드를 작성
# 검색
u = "Bing is awesome"
l = "a", "e", "i", "o" ,"u"
n = 0
for i in u:
    if i in l:
        n += 1
print(n)  