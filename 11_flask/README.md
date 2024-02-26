Flask

* 파이썬 문법 정리

 ## 1.  파이썬 자료형
- 숫자형 - 123
- 문자형 - "word" or 'word'
- 리스트형 - [1, 2, 3, 4, 5]
- 불형 - True, False
- 튜플형, 딕셔너리형, 집합형 - (1,2,3,4,5), {"key":"value",  "key1":"value2"}, set([1,2,3,4,5])


## 2. 파이썬 제어문

### 조건문 - if
```
  (1) 형태
        if 조건문:
        		실행할 코드 ( if 조건문이 참일 때)
        elif 조건문:
        		실행할 코드 ( elif 조건문이 참일 때)
        else: # 있어도 되고 없어도 된다.
        		실행할 코드 (모든 if, elif 조건문이 거짓일 때)

  (2) 비교연산자
        - a와 b가 같다 : a == b
        - a와 b가 같지 않다 : a != b
        - a가 b보다 작다 : a < b
        - a가 b보다 작거나 같다 : a <= b
        - a가 b보다 크다 : a > b
        - a가 b보다 크거나 같다 : a >= b
        - and, or 추가할 수도 있다.

    weight = 100 # 100이라는 값을 weight 변수에 담겠다.
    weight == 100 # weight라는 값이 100이라는 값과 같은가? -> 같으면: True, 다르면: False

  (3) and, or
```

### 반복문 - for, while
```
  (1) for
      for i in range(1000):
      	print(i) # 0~999까지
      
      cities = ["seoul", "daejeon", "daegu", "busan"] # 대괄호 []
      for city in cities:
      		print(city) # seoul, daejeon ...
      		if city == "seoul":
      			print("")
      
      for data in datas:

 (2) while
      while 조건문:
      		실행할 문장
      
      i=0
      while i < 10:
      	i += 1
      
      *조건문이 참인 경우에 문장이 반복되서 실행
```


### continue, break

    반복되는 문장에서 건너뛰고 싶을 땐 ⇒ continue
    
    반복을 멈추고 싶을 땐 ⇒ break





## 3. 파이썬 함수와 클래스
```
   (1) 함수 (def)
   반복적으로 생성되는 코드들을 재활용하여 사용하고 싶을 때 사용
   
   def 함수명(매개변수): 
   		실행할 문장
   
   함수명(인수)
   
   def Name(name):
   	return name
   
   Name()
   
   
   (2) 클래스
   하나의 틀이다. 데이터 저장 기능

   class FishBread:
   		name = "팥붕어빵"
   		def redbean_bread(self):
   			print("이 붕어빵은 " + self.name + " 입니다.")
   
   		def black_bread(self):
   			print("이 붕어빵은 " + self.name + " 입니다.")
   
   FishBread.redbean_bread()
   FishBread.black_bread()
   
   a = FishBread() # 클래스 호출
   type(a) # 클래스
   
   a.redbean_bread() # 클래스 내 함수(메소드)에 접근
   a.black_bread("블랙")
   a.name # 클래스 내 변수(속성)에 접근
   ```
