transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

# 1. Xóa khoảng trắng thừa 2 đầu chuỗi - PHẢI gán lại vì chuỗi là bất biến
transaction = transaction.strip()

# 2. Tách theo ĐÚNG dấu phân cách "|" (dấu "-" nằm bên trong mã khóa học "PYTHON-01")
parts = transaction.split("|")

# 3. Mỗi phần sau khi tách còn dính khoảng trắng quanh dấu "|" -> strip() từng phần
student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()
amount = int(parts[2].strip())          # chuyển sang số để định dạng tiền
status = parts[3].strip().upper()

print(f"Học viên: {student_name}")
print(f"Khóa học: {course_code}")
print(f"Số tiền: {amount:,} VND")       # 15000000 -> 15,000,000
print(f"Trạng thái: {status}")
