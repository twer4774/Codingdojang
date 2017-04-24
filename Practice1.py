"""1~1000에서 각 숫자의 개수 구하기

예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5

그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개 """


result = {x:0 for x in range(0,10)} # 0~9까지의 딕셔너리공간을 만든다

for n in range(1, 1001): # 1부터 1000까지 숫자가 증가한다
    for i in str(n): # 각 숫자를 str()함수를 이용해 숫자를 문자형태로 변환한다(슬라이싱을 하기 위해).
        result[int(i)] += 1 # 나온 숫자를 배열의 인덱스 값에 맞추어 추가한다. int()함수를 이용해 숫자형태로 딕셔너리에 넣는다
print(result)   # 출력으로 결과를 확인한다



