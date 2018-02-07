## Chuẩn ban đầu

from turtle import *

shape('turtle')
speed(0)
# i khí giải thích
for i in range(80): # i đại diện cho các hành động của đối tượng ngay dưới ???
    forward(100)
    left(90)
mainloop()

## Dùng i
# Dùng i Cách 1
from turtle import *

shape('turtle')
speed(0)

for i in range(0, 80, 4):
    # Cách 2 range(80) forward(i * 3)/ forward(i * 3 + 10) lượng ban đầu thêm tâm to
    forward(i)
    left(90)
mainloop()

# Dùng i Cách 2

from turtle import *
shape('turtle')
speed(0)

for i in range(80):
    forward(i * 3 + 10)
    left(90)
mainloop()

## Thiếu thôn tin dùng têm biến tăng dần length
from turtle import *
shape("turtle")
speed(0)
length(10)
for i in range(80):
    forward(length)
    lengh =+ 5 # tăng sau mỗi lần lặp số nào đó
    left(90)

# Chưa hiểu đoạn C4E15 Session2 part2 10:00 phút
