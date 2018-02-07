yob = int(input("Your year of birthday? ")) # mời nhập vào convert là INT lưu vào biến yob
age = 2018 - yob # lấy năm hiển tại trừ đi nó / lưu kq dấu trừ bào biến age
print("Your age", age) # in từ tuôi và in biến mới age là tuổi

if age < 10: # gặp if là kiến tra
    print("Baby")
elif age <18: # biến thể cuổi cùng của cld kiện viết tắt else if
    print("Teenager")
else:
    print("Adult")

# Thêm
# đây là một cấu trúc vòng lặp riêng đã hoàn thành nhiệm vụ
if age < 10:
    print("Baby")
# đây là một cấu trúc vòng lặp riêng đã hoàn thành nhiệm vụ
if 10 <= age <18: # Đúng vì nó ko có sự trợ giúp của thằng bên trên rùi
    print("Teenager") # Dấu = là của <18
else:
    print("Adult")

# if chỉ chạy khi điểu kiện đằng sau ì thỏa mãn điều kiện mà thôi
    # câu lệnh rẽ nhanh chỉ chạy 1 trg hợp thui, và có những phần sẽ kobg chạy
# Các dev luôn tìm cách để cho chạy qua các nhánh cho phòng tránh các lỗi về sau
    # nên là cố cave bao hết các nhánh có độ phủ 100%
# Test 3 lần đủ phủ 100%
# gặp if là kiến tra, là tạo thêm các nhánh của các bước, chạy 1 sẽ ko chạy thêm
