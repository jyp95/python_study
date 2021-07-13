# 4.1 리스트와 반복문
print()
# 리스트 특정 요소 변경
list_a = [1, 2, 3, "안녕", True, False]
print(list_a)
print()
list_a[0] = "변경"
print(list_a)
print()
# 리스트 안에 리스트 사용
list_b = [[1,2,3], [4,5,6], [7,8,9]]
print(list_b[1])
print(list_b[1][0])
print()
# append()함수 이용하여 리스트에 요소 추가
list_c = [1, 2, 3]
print("# 리스트 뒤에 요소 추가")
list_c.append(4)
list_c.append(5)
print(list_c)
print()
# insert()함수 이용하여 리스트에 요소 추가
list_c.insert(0, 100)
print(list_c)
print()
# in/not in 연산자 활용하여 리스트 내부에 특정 값 있는지 확인
list_d = [123, 321, 59]
print(49 in list_d)
print(98 not in list_d)
print()
# for 반복문
for i in range(10):
    print("출력")
print()