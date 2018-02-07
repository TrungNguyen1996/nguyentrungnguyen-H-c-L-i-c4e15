# Cách tính tổng 1
# gốc 1:
n = int(input("Enter a number?"))
for i in range(n + 1): # luôn từ 1 trở lên
    print(i)

# tính tỏng các số trong vòng lặp

# Thêm
## khúc 1
n = int(input("Enter a number?"))

total = 0 # Cho rổ hửng từ đầu trống sạch bằng 0
## khúc 2
for i in range(n + 1):
    # total = 0 là ko dc, mỗi lần chạy là tổng về 0 khi chạy for
    total += i
    # total = total + i/ công dồn i sau mỗi lần lặp bao giờ cho hết vòng lặp thì thôi
## khúc 3
print(total) # in ngoài vòng for để sau khi hứng hết táo mới khoe ra
# vs 3 khúc như này sau làm seach là gi gì thì sẽ liên quan đến vòng for như này
# đây là cách làm tổng quát mó sẽ đúng cho ko chỉ python và vs tát cả ngôn ngữ lập trình khác
