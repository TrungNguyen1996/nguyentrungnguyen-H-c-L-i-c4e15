from getpass import getpass # từ thư viện getpass nhập vào hàm getpass
usename = input("Usename: ") # là string luôn rùi ko cần int
password = getpass("password: ") # input hiện bth/ getpass ẩn ký tự
if usename == "c4e": # so sánh mà giống thì vào trong đi tiép
    if password == "codethechange":
        # pass bỏ qua nếu chưa cần chạy/ nếu pass so sánh đúng chào và vào trong
        print("Welcome, c4e")# pa4ss
    ##### nẾU SAI mật khẩu thì báo " Wrong "
    else:
        print("Wrong password")
#### Nếu tên đăng nhập ko đúng thì báo sao tên
else:
    print("Nosuch user, go away")
# Thêm để ko bị nhìn thấy password seach: pythonn 3 input without echoing
# echo làm cho viết đâu hiện đấy, thiếu echo ko hiện kí tự nhập vào
# Dùng hàm và là cả thư viện luôn getpass()
