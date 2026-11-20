# Bài 2 - [Vận dụng cơ bản] Lỗi chuẩn hóa thông tin học viên

## Đề bài

Rikkei Education xây dựng hệ thống quản lý học viên đăng ký khóa học. Mỗi học viên nhập Họ và tên, Mã học viên, Email liên hệ. Trước khi lưu, dữ liệu cần được chuẩn hóa:

- **Họ tên:** xóa khoảng trắng hai đầu và viết hoa chữ cái đầu mỗi từ.
- **Mã học viên:** xóa khoảng trắng hai đầu và viết hoa toàn bộ.
- **Email:** xóa khoảng trắng hai đầu và viết thường toàn bộ.

Kết quả đúng cần hiển thị:

```
Họ tên: Nguyen Van A
Mã học viên: RK-001-PYTHON
Email: student01@gmail.com
```

**Vấn đề:** lập trình viên đã gọi `.strip()`, `.title()`, `.upper()`, `.lower()` nhưng kết quả **vẫn chưa được chuẩn hóa**, vì quên rằng **chuỗi trong Python có tính bất biến**: các phương thức trên không thay đổi trực tiếp chuỗi gốc mà **trả về một chuỗi mới**.

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py) *(gõ lại từ ảnh đề bài)*

```python
student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name.strip()
student_name.title()

student_code.strip()
student_code.upper()

email.strip()
email.lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)
```

Kết quả trên Console (dữ liệu vẫn còn khoảng trắng và sai chữ hoa/thường):

```
Họ tên:   nguYEn vAn a  
Mã học viên:   rk-001-python  
Email:   Student01@GMAIL.COM
```

## (1) Phân tích lỗi

**Vì sao `student_name.strip()` không làm thay đổi trực tiếp biến `student_name`?**
Chuỗi (`str`) là kiểu **bất biến (immutable)**: sau khi tạo thì không thể sửa nội dung bên trong. `strip()` không "cắt" chuỗi cũ mà tạo ra **một chuỗi mới** đã bỏ khoảng trắng rồi **trả về** chuỗi đó. Câu lệnh `student_name.strip()` đứng một mình không gán kết quả cho biến nào, nên chuỗi mới bị **bỏ đi ngay**; biến `student_name` vẫn trỏ tới chuỗi gốc.

**Vì sao `student_name.title()` không tạo ra kết quả `"Nguyen Van A"`?**
Cùng nguyên nhân: `title()` trả về chuỗi mới `"  Nguyen Van A  "` nhưng kết quả không được lưu lại. Hơn nữa, dòng này được gọi trên **chuỗi gốc** (vì kết quả của `strip()` ở dòng trước đã mất), nên dù có lưu thì vẫn còn khoảng trắng hai đầu.

**Vì sao `student_code.upper()` không làm mã học viên chuyển thành chữ hoa?**
`upper()` trả về `"  RK-001-PYTHON  "` nhưng không gán lại cho `student_code`, nên khi in vẫn là chuỗi gốc `"  rk-001-python  "`.

**Vì sao `email.lower()` không làm email chuyển thành chữ thường?**
Tương tự, `lower()` tạo chuỗi mới viết thường rồi bỏ đi; `email` vẫn là `"  Student01@GMAIL.COM  "`.

**Muốn các phương thức xử lý chuỗi có hiệu lực, cần làm gì?**
**Gán kết quả trả về lại cho biến** (hoặc cho một biến mới), ví dụ `student_name = student_name.strip()`. Có thể **nối chuỗi phương thức** (method chaining) để gọn hơn: `student_name.strip().title()`. Python thực hiện từ trái sang phải: `strip()` trả về chuỗi mới, rồi `title()` được gọi trên chính chuỗi mới đó.

> Python không báo lỗi vì gọi phương thức mà không dùng kết quả là hoàn toàn hợp lệ về cú pháp. Đây là **lỗi logic**.

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
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
```

## Kết quả

```
Họ tên: Nguyen Van A
Mã học viên: RK-001-PYTHON
Email: student01@gmail.com
```

| Biến | Trước | Sau |
|---|---|---|
| `student_name` | `"  nguYEn vAn a  "` | `"Nguyen Van A"` ✅ |
| `student_code` | `"  rk-001-python  "` | `"RK-001-PYTHON"` ✅ |
| `email` | `"  Student01@GMAIL.COM  "` | `"student01@gmail.com"` ✅ |
