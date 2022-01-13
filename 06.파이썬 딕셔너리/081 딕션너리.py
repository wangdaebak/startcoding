# 081 별 표현식 
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, m1, m2 =scores # 언패킹설명 https://blog.naver.com/sunghak93/222610911346 # 언패킹 과정에서  *(Asterisk) 활용하기
print(valid_score)

# 082 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
m1, m2, *valid_score = scores  # 우측 8개값을 바인딩 해야하기때문에 *(Asterisk)을 마지막에 넣어줌
print(valid_score)

# 083 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
m1, *valid_score, m2 = scores
print(valid_score)

# 084 비어있는 딕셔너리
temp = {}
print(temp)

# 085 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.

item = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(item)

# 086 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
item['죠스바'] = 1200
item['월드콘'] = 1500  # 두 줄쓰기로 해야 오류가 안생김
print(item)

# 087 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
print(item['메로나'])  # 가격을 출력해야하기때문에 [] 기호를 사용할것

# 088 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
item['메로나'] = 1300
print(item['메로나'])  # 딕셔너리 값 수정, key추가,제거, 딕셔너리 값 초기화, 딕셔너리 만들고 값 가져오기가 가능

# 089 다음 딕셔너리에서 메로나를 삭제하라.
del item['메로나']
print(item)

# 090 다음 코드에서 에러가 발생한 원인을 설명하라.
'''
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
'''
# 090 정답 > 누가바라는 키값이 없기때문에 value을 인덱싱할 수 없다.

# 091 딕셔너리 생성 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
inventory = {"메로나":[300,20], "비비빅":[400,3],"죠스바":[250,100]}
print(inventory)

# 092 딕셔너리 인덱싱 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print(inventory['메로나'][0])


# 093 딕셔너리 인덱싱 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory['메로나'][1])

# 094 딕셔너리 추가 
inventory["월드콘"] =[500,7]
print(inventory)

# 095 딕셔너리 keys() 메서드 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys())) # 리스트로 출력
print(icecream.keys()) # dict_keys 출력 #형변환을 하려면 위에처럼 형변환 자료형으로 바꿔줘야한다

# 096 딕셔너리 values() 메서드 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.values()))

# 098 딕셔너리 update 메서드 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099 zip과 dict 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))  # zip함수를 사용하여 dict로 출력 # https://chancoding.tistory.com/144?category=823356
print(result)

result = list(zip(keys,vals))  # zip함수를 사용하여 list로 출력 # https://chancoding.tistory.com/144?category=823356
print(result)

result2 = list(zip(*result))
print(result)  # zip 함수 활용 1. 전치행렬 생성하기 (a 리스트의 각 요소인 리스트 들을 zip으로 묶어줄 수 있습니다. 이를 통해서 transform 한 것과 같은 효과를 확인할 수 있습니다.)
               # 대체 전치행렬이 뭐에요?(result에서 result2로 이동한 느낌입니다.)

a = ['one', 'two', 'three']  # 딕셔너리 ZIP함수 사용(반복문 활용방법) https://chancoding.tistory.com/144?category=823356
b = ['a', 'b', 'c']
print(list(zip(a, b)))  # a라는 리스트와 b라는 리스트의 값들이 index 순서에 따라서 묶어진 것을 확인할 수 있습니다.
for val1, val2 in zip(a, b):
    print(val1, val2)  # ZIP 반복문에서 특히나 활용하기가 좋습니다. 반복문을 수행할 때, 두 개의 리스트의 값을 각각 가져와야 할 경우 매우 유용하게 사용할 수 있습니다.

# 100 zip과 dict date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price)) # dict 출력
print(close_table)

close_table =list(zip(date,close_table)) # list 출력
print(close_table)