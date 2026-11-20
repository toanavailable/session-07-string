# Bài 3 - [Vận dụng cơ bản] Lỗi xử lý mã giao dịch học phí

## Đề bài

Rikkei Education quản lý giao dịch học phí của học viên. Mỗi giao dịch được nhập dưới dạng một chuỗi có cấu trúc:

```
Tên học viên | Mã khóa học | Số tiền | Trạng thái
```

Ví dụ: `transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "`

Hệ thống cần chuẩn hóa và hiển thị:

```
Học viên: Nguyen Van A
Khóa học: PYTHON-01
Số tiền: 15,000,000 VND
Trạng thái: PAID
```

**Yêu cầu xử lý:** xóa khoảng trắng thừa ở hai đầu chuỗi; tách chuỗi giao dịch theo dấu `|`; chuẩn hóa tên học viên bằng `.title()`; chuẩn hóa trạng thái bằng `.upper()`; định dạng số tiền có dấu phẩy phân cách hàng nghìn.

**Vấn đề:** lập trình viên đã dùng `.strip()`, `.split()`, `.title()`, `.upper()` nhưng kết quả vẫn sai. Các lỗi logic: gọi `.strip()` nhưng không gán lại kết quả; dùng sai dấu phân cách khi tách chuỗi; lấy sai vị trí dữ liệu sau khi tách; chưa chuẩn hóa riêng từng phần dữ liệu.

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py) *(gõ lại từ ảnh đề bài)*

```python
transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction.strip()

parts = transaction.split("-")

student_name = parts[0].title()
course_code = parts[1]
amount = parts[2]
status = parts[3].upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount, "VND")
print("Trạng thái:", status)
```

Kết quả khi chạy, chương trình **dừng vì lỗi**:

```
Traceback (most recent call last):
  File "script_legacy.py", line 9, in <module>
    amount = parts[2]
             ~~~~~^^^
IndexError: list index out of range
```

## (1) Phân tích lỗi

**Vì sao `transaction.strip()` không làm thay đổi trực tiếp chuỗi ban đầu?**
Chuỗi là **bất biến**. `strip()` trả về một **chuỗi mới** đã bỏ khoảng trắng, nhưng câu lệnh không gán kết quả cho biến nào nên chuỗi mới bị bỏ đi; `transaction` vẫn còn khoảng trắng ở hai đầu. Phải viết `transaction = transaction.strip()`.

**Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?**
Bằng dấu **`|`** (gạch đứng), theo cấu trúc `Tên học viên | Mã khóa học | Số tiền | Trạng thái`.

**Vì sao `transaction.split("-")` là sai?**
Dấu `-` **không phải** ký tự phân cách giữa các trường. Nó là một phần **bên trong** dữ liệu (mã khóa học `PYTHON-01`). Tách theo `-` sẽ cắt chuỗi ở giữa mã khóa học, sai hoàn toàn cấu trúc.

**Sau khi tách bằng sai delimiter, dữ liệu trong `parts` bị lệch như thế nào?**

```python
parts = ["  nguyEN vAn a | PYTHON", "01 | 15000000 | paid  "]
```

| Biến | Mong đợi | Thực tế với `split("-")` |
|---|---|---|
| `parts[0]` | Tên học viên | `"  nguyEN vAn a | PYTHON"`: tên **dính** cả nửa đầu mã khóa học |
| `parts[1]` | Mã khóa học | `"01 | 15000000 | paid  "`: nửa sau mã khóa học **dính** số tiền và trạng thái |
| `parts[2]` | Số tiền | **Không tồn tại**: danh sách chỉ có 2 phần tử nên `parts[2]` gây `IndexError: list index out of range` |
| `parts[3]` | Trạng thái | **Không tồn tại** |

**Vì sao cần `.strip()` lại từng phần sau khi `split()`?**
`split("|")` chỉ cắt đúng tại ký tự `|`; các khoảng trắng nằm **quanh** dấu `|` vẫn còn dính vào từng phần: `["nguyEN vAn a ", " PYTHON-01 ", " 15000000 ", " paid"]`. Nếu không `strip()` thì tên in ra thừa khoảng trắng, mã khóa học không khớp khi so sánh, và `int(" 15000000 ")` tuy vẫn chạy được nhưng dữ liệu không sạch để lưu trữ.

**Vì sao cần chuyển `amount` từ chuỗi sang số trước khi định dạng tiền?**
Định dạng phân cách hàng nghìn `{:,}` chỉ áp dụng cho **số** (`int`, `float`). Với chuỗi `"15000000"`, `f"{amount:,}"` báo lỗi `ValueError: Cannot specify ',' with 's'`. Vì vậy phải `int(...)` trước, sau đó `f"{amount:,}"` mới cho ra `15,000,000`. Lưu dạng số cũng giúp tính toán được (cộng tổng doanh thu, so sánh…).

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
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
```

Thay đổi:
1. **Gán lại** kết quả `strip()` cho `transaction`.
2. Tách theo **đúng delimiter** `"|"`.
3. **`strip()` từng phần** sau khi tách; chuẩn hóa tên bằng `title()`, mã khóa học và trạng thái bằng `upper()`.
4. Chuyển số tiền sang `int` rồi định dạng `{amount:,}`.

## Kết quả

```
Học viên: Nguyen Van A
Khóa học: PYTHON-01
Số tiền: 15,000,000 VND
Trạng thái: PAID
```
