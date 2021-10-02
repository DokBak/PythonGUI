kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(zip(kor,eng)) # 두개의 리스트에서 인덱스가 같은 것끼리 묶어줄때 사용한다.
print(list(zip(kor,eng))) # list가 없는경우 오브젝트 타입만 표시하기에 추가 작성

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # *를 붙여 줌으로써 묶어주는 zip()과는 달리 분리 해주는 역할

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)