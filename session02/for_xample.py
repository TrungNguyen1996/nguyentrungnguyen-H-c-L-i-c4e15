# stat stop step
# 1
for i in range(2, 5):
    print("Hello")
print("Bye")
# 2
for i in range(2, 8, 3): # ??? con chạy for _ in range vòng chua dung den
    #range(2, 5):
    print("Hello")
print("Bye")
# 3
for i in range(2, 5, 0):
    print("Hello")
print("Bye")
# 4
for i in range(5): #range(1, 2, 3, 4, 5)
    print(i)
print("Bye")
# 4
x = 5
for i in range(x):
    print(i)

# # hỏi start step stop

# i là itertor

for i in range(5): # 3 quy tắc
    print("Hello") # phụ thuộc vòng for
print("Bye")
#
for i in range(2, 8, 3): # ???
    print(i) # phụ thuộc vòng for
print("Bye")
#
for i in range(2, 8, 3): # ???
    print("Hello") # phụ thuộc vòng for
print("Bye")
#
for i in range(2, 8, 3): # ??? stat stop step
    print("i") # phụ thuộc vòng for
print("Bye")
#
for i in range(2, 8, 3): # ???
    print("i") # phụ thuộc vòng for
print("Bye")
