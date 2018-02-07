from turtle import * # tên biến ko dc trùng tên file / nhập vào thư viện con rùa / * dùng tất cả hành động trong thư viện con rùa
speed(0)
color("green") # ??? color
shape("turtle") # là biến đối tượng mặc định thành hình con rùa trong thư viện con rùa
for i in range(3):      # range(300) left(7) - 360 ko chia het 7 - ko trùng hình/Sau for là một biến/ : đặc trưng của lặp lại
    forward(100)
    left(90)

    forward(100)
    left(90)

    forward(100)
    left(90)

    forward(100)

    left(7)

mainloop() # Giữ màn hình chạy

# Không được đặt tên biến trùng vs tên file tạo vong lặp vô hạn Lỗi!
