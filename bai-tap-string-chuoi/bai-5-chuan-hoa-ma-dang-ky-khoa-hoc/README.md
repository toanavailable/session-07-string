# Bài 5 - [Vận dụng chuyên sâu] Hệ thống chuẩn hóa mã đăng ký khóa học

## Đề bài

Tại Rikkei Education, học viên đăng ký khóa học qua nhiều kênh (website, fanpage, tư vấn viên, biểu mẫu online) nên thông tin đăng ký thường không đồng nhất:

```
"  nguyEN van a | python basic | rk-001 | student01@GMAIL.com  "
```

Dữ liệu gồm 4 phần: `Họ tên học viên | Tên khóa học | Mã học viên | Email`. Các vấn đề: họ tên thừa khoảng trắng và viết hoa lộn xộn; tên khóa học chưa chuẩn hóa; mã học viên chưa viết hoa đồng nhất; email có chữ hoa, không đúng định dạng chuẩn lưu trữ; toàn bộ thông tin nằm trong một chuỗi duy nhất, cần tách ra để xử lý.

**Yêu cầu nghiệp vụ:** người dùng nhập số lượng phiếu đăng ký cần xử lý; với mỗi phiếu nhập một chuỗi theo định dạng trên. Sau khi nhập, hệ thống chuẩn hóa và in:

```
===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====
Học viên: Nguyen Van A
Khóa học: Python Basic
Mã học viên: RK-001
Email: student01@gmail.com
Mã xác nhận: RK-001_PYTHON-BASIC
```

**Edge cases:**

| Bẫy | Điều kiện | Thông báo | Hành động |
|---|---|---|---|
| 1 | Số lượng phiếu `<= 0` | `Số lượng phiếu đăng ký không hợp lệ` | Kết thúc chương trình |
| 2 | Tách bằng `|` không đủ 4 phần | `Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này` | Bỏ qua phiếu, sang phiếu tiếp |
| 3 | Email sau chuẩn hóa không chứa `@` | `Email không hợp lệ. Bỏ qua phiếu này` | Bỏ qua phiếu |
| 4 | Mã học viên sau chuẩn hóa quá ngắn | `Mã học viên không hợp lệ. Bỏ qua phiếu này` | Bỏ qua phiếu |

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Chuẩn hóa | Kết quả mẫu |
|---|---|---|---|---|
| Số lượng phiếu | `form_count` | `int` | Kiểm tra `isdigit()` và `> 0` | `6` |
| Chuỗi phiếu thô | `raw_form` | `str` | `split("|")` → 4 phần | |
| Họ tên | `student_name` | `str` | Bỏ khoảng trắng thừa + `title()` | `Nguyen Van A` |
| Tên khóa học | `course_name` | `str` | Bỏ khoảng trắng thừa + `title()` | `Python Basic` |
| Mã học viên | `student_code` | `str` | `strip().upper()` | `RK-001` |
| Email | `email` | `str` | `strip().lower()` | `student01@gmail.com` |
| Mã xác nhận | `confirm_code` | `str` | Mã HV + `_` + tên khóa học `upper()`, `replace(" ", "-")` | `RK-001_PYTHON-BASIC` |

### Đề xuất giải pháp

- **Vòng lặp:** số phiếu biết trước nên dùng `for form_number in range(1, form_count + 1)`.
- **Bẫy 1** kiểm tra **trước** vòng lặp; dùng `isdigit()` nên gõ chữ hoặc số âm cũng được bắt, không crash.
- **Bẫy 2:** `parts = raw_form.split("|")` rồi kiểm tra `len(parts) != 4`; sai thì `continue`.
- **Bẫy 3:** toán tử `in`: `"@" not in email` thì `continue`.
- **Bẫy 4:** `len(student_code) < 5` thì `continue`. Mã chuẩn dạng `RK-001` dài 6 ký tự; ngưỡng đặt ở biến `min_code_length` để dễ chỉnh.
- Thứ tự kiểm tra: **cấu trúc** (Bẫy 2) trước, vì phải đủ 4 phần mới tách được email và mã; sau đó chuẩn hóa rồi mới kiểm tra **nội dung** (Bẫy 3, 4).
- `" ".join(s.split())` dọn được cả khoảng trắng thừa **ở giữa** (VD: `"data   science"` → `"data science"`).

### Thiết kế thuật toán (Pseudocode)

```
NHẬP form_count_text
NẾU form_count_text không phải số nguyên dương:
    IN "Số lượng phiếu đăng ký không hợp lệ" → KẾT THÚC
LẶP form_number TỪ 1 ĐẾN form_count:
    NHẬP raw_form
    parts ← raw_form.split("|")
    NẾU số phần != 4: IN "Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này"; TIẾP TỤC
    student_name ← title(chuẩn hóa khoảng trắng(parts[0]))
    course_name  ← title(chuẩn hóa khoảng trắng(parts[1]))
    student_code ← upper(strip(parts[2]))
    email        ← lower(strip(parts[3]))
    NẾU "@" không có trong email: IN "Email không hợp lệ. Bỏ qua phiếu này"; TIẾP TỤC
    NẾU độ dài student_code < 5: IN "Mã học viên không hợp lệ. Bỏ qua phiếu này"; TIẾP TỤC
    confirm_code ← student_code + "_" + upper(course_name) thay " " bằng "-"
    IN phiếu đăng ký đã chuẩn hóa
```

## (2) Triển khai code

File: [`chuan_hoa_dang_ky.py`](chuan_hoa_dang_ky.py)

```python
"""Hệ thống chuẩn hóa mã đăng ký khóa học - Rikkei Education."""

min_code_length = 5   # mã học viên chuẩn (VD: RK-001) tối thiểu 5 ký tự

# ========== NHẬP SỐ LƯỢNG PHIẾU ==========
form_count_text = input("Nhập số lượng phiếu đăng ký cần xử lý: ").strip()

# Bẫy 1: số lượng phiếu <= 0 (hoặc không phải số) -> kết thúc chương trình
if not form_count_text.isdigit() or int(form_count_text) <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    form_count = int(form_count_text)

    for form_number in range(1, form_count + 1):
        print(f"\n--- Phiếu đăng ký {form_number} ---")
        raw_form = input("Nhập: Họ tên | Tên khóa học | Mã học viên | Email\n> ")

        # Bẫy 2: tách theo "|" phải được đúng 4 phần
        parts = raw_form.split("|")
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        # Chuẩn hóa từng phần
        student_name = " ".join(parts[0].split()).title()     # "Nguyen Van A"
        course_name = " ".join(parts[1].split()).title()      # "Python Basic"
        student_code = parts[2].strip().upper()               # "RK-001"
        email = parts[3].strip().lower()                      # "student01@gmail.com"

        # Bẫy 3: email phải chứa "@"
        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        # Bẫy 4: mã học viên quá ngắn
        if len(student_code) < min_code_length:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        # Mã xác nhận: Mã học viên + "_" + Tên khóa học IN HOA, khoảng trắng thay bằng "-"
        confirm_code = student_code + "_" + course_name.upper().replace(" ", "-")

        print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {student_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_code}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirm_code}")
```

## Kết quả

Kiểm thử 6 phiếu: hợp lệ → thiếu phần (Bẫy 2) → email sai (Bẫy 3) → mã quá ngắn (Bẫy 4) → hợp lệ có khoảng trắng thừa ở giữa → thừa phần (Bẫy 2):

```
Nhập số lượng phiếu đăng ký cần xử lý: 6

--- Phiếu đăng ký 1 ---
Nhập: Họ tên | Tên khóa học | Mã học viên | Email
>   nguyEN van a | python basic | rk-001 | Student01@GMAIL.com  
===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====
Học viên: Nguyen Van A
Khóa học: Python Basic
Mã học viên: RK-001
Email: student01@gmail.com
Mã xác nhận: RK-001_PYTHON-BASIC

--- Phiếu đăng ký 2 ---
Nhập: Họ tên | Tên khóa học | Mã học viên | Email
> tran b | java | rk-002
Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này

--- Phiếu đăng ký 3 ---
Nhập: Họ tên | Tên khóa học | Mã học viên | Email
> le c | web dev | rk-003 | cgmail.com
Email không hợp lệ. Bỏ qua phiếu này

--- Phiếu đăng ký 4 ---
Nhập: Họ tên | Tên khóa học | Mã học viên | Email
> pham d | sql | rk | d@gmail.com
Mã học viên không hợp lệ. Bỏ qua phiếu này

--- Phiếu đăng ký 5 ---
Nhập: Họ tên | Tên khóa học | Mã học viên | Email
>   hoang   thi e |data   science| rk-005 |E@Mail.Com
===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====
Học viên: Hoang Thi E
Khóa học: Data Science
Mã học viên: RK-005
Email: e@mail.com
Mã xác nhận: RK-005_DATA-SCIENCE

--- Phiếu đăng ký 6 ---
Nhập: Họ tên | Tên khóa học | Mã học viên | Email
> a|b|c|d|e
Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này
```

**Bẫy 1: số lượng phiếu không hợp lệ:**

```
Nhập số lượng phiếu đăng ký cần xử lý: 0
Số lượng phiếu đăng ký không hợp lệ
```

> Ghi chú: ở Bẫy 4, ảnh đề bị mờ đúng chỗ con số độ dài tối thiểu. Mình chọn `5` vì mã chuẩn dạng `RK-001` dài 6 ký tự. Nếu đề gốc dùng số khác, chỉ cần sửa biến `min_code_length` ở đầu file.
