student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

# Chuỗi là bất biến: các phương thức trả về CHUỖI MỚI -> phải gán lại kết quả
student_name = student_name.strip().title()   # xóa khoảng trắng 2 đầu + viết hoa chữ cái đầu
student_code = student_code.strip().upper()   # xóa khoảng trắng 2 đầu + viết hoa toàn bộ
email = email.strip().lower()                 # xóa khoảng trắng 2 đầu + viết thường toàn bộ

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)
