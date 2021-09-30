# 리스트의 reverse(), reversed()차이
lst = [1,2,3,4,5,]
print(lst)

lst.reverse()
print(lst)

lst2 = [2,3,4,5,6]
print("리스트 2 뒤집기 전 : ", lst2)

lst3 = reversed(lst2)
print("리스트 2 뒤집은 후 : ", lst2)
print("리스트3 : ",list(lst3))
