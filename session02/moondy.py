# Bước nhảy ok
from random import randint
num = randint(0, 100)
ok = '''(̶◉͛‿◉̶)'''
sad = '''( ˘︹˘ )'''

if num <30:
    print(sad) # ("I feel sad")
elif num < 60:
    print(ok) 
else:
    print("Let's rock & roll")

# Ví dự thêm:

# from ramdom import randint
# # num = randin(0, 100)
# if randin(0, 100) <30:
#     print("I feel sad")
# elif randin(0, 100) < 60:
#     print("OK")
# else:
#     print("Let's rock & roll")

# Mỗi randint là một lần chạy,sau mỗi lần chạy khai báo một số khác nhau
# khi mà dùng một số lưu nó vào một cái biến, rồi mang cái biến đấy đi dùng
# chứ không bao giờ được mang đi in ra nhiều lần ở các biểu thưc khác nhau cả
