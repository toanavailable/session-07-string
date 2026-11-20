# Bài 1 - [Bài tập tổng hợp] Xây dựng hệ thống chuẩn hóa và tạo thẻ thành viên

## Đề bài

**Mục tiêu:** tích hợp các thao tác xử lý chuỗi (`split`, `strip`, `replace`, `upper`, `title`, f-string) vào một chương trình có tính tương tác; dùng vòng lặp `while` xây dựng menu điều hướng liên tục; kiểm soát luồng khi người dùng nhập sai.

**Bối cảnh:** câu lạc bộ cần công cụ Console để xử lý nhanh thông tin đăng ký thô của thành viên. Chương trình duy trì trạng thái hoạt động liên tục, cho phép chọn các chức năng kiểm tra dữ liệu gốc, chuẩn hóa hiển thị hoặc tạo thông tin tự động.

**Dữ liệu đầu vào:** `raw_input = "   nGuyen vaN aN  ;  2004   "`

| Chức năng | Yêu cầu |
|---|---|
| 1 | In trực tiếp biến `raw_input` để kiểm tra dữ liệu thô |
| 2 | Bóc tách Họ tên và Năm sinh (phân tách bởi `;`); bỏ khoảng trắng thừa, viết hoa chữ cái đầu từng từ (Title Case); tính tuổi (giả định năm hiện tại là **2026**) |
| 3 | Bóc tách Họ, Tên đệm, Tên chính, Năm sinh. **Email:** chữ cái đầu của Họ + chữ cái đầu của Tên đệm + Tên chính, viết thường, thêm `@company.com` (VD: `nvan@company.com`). **Mã ID:** Tên chính viết hoa + 2 số cuối năm sinh bằng slicing (VD: `AN04`). In "Thẻ thành viên" vuông vức bằng f-string căn lề |
| 4 | In lời chào và kết thúc chương trình |
| Ngoại lệ | Nhập ký tự lạ hoặc số ngoài 1-4: in `Lựa chọn không hợp lệ, vui lòng nhập lại!` và hiện lại menu |

## Phân tích

| Bước | Kỹ thuật | Ví dụ |
|---|---|---|
| Tách Họ tên và Năm sinh | `raw_input.split(";")` | `["   nGuyen vaN aN  ", "  2004   "]` |
| Bỏ khoảng trắng thừa (kể cả giữa các từ) | `" ".join(name_part.split())` | `"nGuyen vaN aN"` |
| Title Case | `.title()` | `"Nguyen Van An"` |
| Năm sinh | `year_part.strip()` rồi `int()` | `2026 - 2004 = 22` |
| Tách Họ / Tên đệm / Tên chính | `words = full_name.split()`; `words[0]`, `words[1:-1]`, `words[-1]` | `"Nguyen"`, `["Van"]`, `"An"` |
| Email | chữ cái đầu `[0]` + `.lower()` | `"n" + "v" + "an"` → `nvan@company.com` |
| Mã ID | `.upper()` + slicing `[-2:]` | `"AN" + "04"` → `AN04` |
| Thẻ thành viên | f-string `{:^40}`, `{:<10}` | Căn giữa tiêu đề, căn trái nhãn |

- `split()` **không tham số** tách theo mọi khoảng trắng liên tiếp và bỏ khoảng trắng ở hai đầu. Kết hợp với `" ".join(...)` sẽ dọn được khoảng trắng thừa **ở giữa** chuỗi, điều mà `strip()` không làm được.
- Tên đệm lấy bằng `words[1:-1]` nên chương trình vẫn đúng khi họ tên có nhiều hơn một tên đệm (VD: "Tran Thi Thu Ha" → `t` + `tt` + `ha` → `tttha@company.com`).
- Menu dùng `while True` + `break` ở lựa chọn 4; lựa chọn giữ dạng chuỗi nên gõ chữ cũng không làm chương trình dừng vì lỗi.

## Lời giải

File: [`the_thanh_vien.py`](the_thanh_vien.py)

```python
"""[Bài tập tổng hợp] Xây dựng hệ thống chuẩn hóa và tạo thẻ thành viên."""

# ========== KHỞI TẠO ==========
raw_input = "   nGuyen vaN aN  ;  2004   "   # chuỗi dữ liệu thô ban đầu
current_year = 2026                            # giả định năm hiện tại
email_domain = "@company.com"
line_width = 40

# ========== VÒNG LẶP MENU ==========
while True:
    print("\n" + "─" * 8 + " HỆ THỐNG XỬ LÝ THÀNH VIÊN " + "─" * 8)
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("─" * (line_width + 3))
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    # ----- Chức năng 1: in trực tiếp chuỗi gốc -----
    if choice == "1":
        print("\nChuỗi dữ liệu gốc hiện tại:")
        print(f"'{raw_input}'")

    # ----- Chức năng 2 và 3 đều cần bóc tách chuỗi gốc -----
    elif choice == "2" or choice == "3":
        # Tách Họ tên và Năm sinh bởi dấu ";"
        name_part, year_part = raw_input.split(";")

        # Chuẩn hóa họ tên: bỏ khoảng trắng thừa (cả ở giữa), viết hoa chữ cái đầu
        full_name = " ".join(name_part.split()).title()   # "Nguyen Van An"
        birth_year_text = year_part.strip()                # "2004"

        if choice == "2":
            age = current_year - int(birth_year_text)
            print("\n[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]")
            print(f"- Họ và tên: {full_name}")
            print(f"- Tuổi hiện tại: {age} tuổi")
        else:
            # Bóc tách Họ, Tên đệm, Tên chính
            words = full_name.split()
            last_name = words[0]                    # Họ: "Nguyen"
            first_name = words[-1]                  # Tên chính: "An"
            middle_initials = ""                    # chữ cái đầu của (các) tên đệm
            for middle_name in words[1:-1]:
                middle_initials += middle_name[0]

            # Email: chữ đầu của Họ + chữ đầu Tên đệm + Tên chính, viết thường
            email = (last_name[0] + middle_initials + first_name).lower() + email_domain
            # Mã ID: Tên chính viết hoa + 2 số cuối năm sinh (slicing)
            member_id = first_name.upper() + birth_year_text[-2:]

            print("\n" + "─" * line_width)
            print(f"{'THẺ THÀNH VIÊN MỚI':^{line_width}}")
            print("─" * line_width)
            print(f"{'Họ và tên':<10}: {full_name}")
            print(f"{'Mã ID':<10}: {member_id}")
            print(f"{'Email':<10}: {email}")
            print("─" * line_width)

    # ----- Chức năng 4: thoát -----
    elif choice == "4":
        print("\nChương trình đã đóng!")
        break

    # ----- Xử lý ngoại lệ: nhập ký tự lạ hoặc số ngoài 1-4 -----
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")
```

## Kết quả

Chạy lần lượt các lựa chọn 1 → 2 → 3 → `x` → `7` → 4:

```

──────── HỆ THỐNG XỬ LÝ THÀNH VIÊN ────────
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
───────────────────────────────────────────
Nhập lựa chọn của bạn (1-4): 1

Chuỗi dữ liệu gốc hiện tại:
'   nGuyen vaN aN  ;  2004   '

──────── HỆ THỐNG XỬ LÝ THÀNH VIÊN ────────
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
───────────────────────────────────────────
Nhập lựa chọn của bạn (1-4): 2

[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]
- Họ và tên: Nguyen Van An
- Tuổi hiện tại: 22 tuổi

──────── HỆ THỐNG XỬ LÝ THÀNH VIÊN ────────
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
───────────────────────────────────────────
Nhập lựa chọn của bạn (1-4): 3

────────────────────────────────────────
           THẺ THÀNH VIÊN MỚI           
────────────────────────────────────────
Họ và tên : Nguyen Van An
Mã ID     : AN04
Email     : nvan@company.com
────────────────────────────────────────

──────── HỆ THỐNG XỬ LÝ THÀNH VIÊN ────────
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
───────────────────────────────────────────
Nhập lựa chọn của bạn (1-4): x

Lựa chọn không hợp lệ, vui lòng nhập lại!

──────── HỆ THỐNG XỬ LÝ THÀNH VIÊN ────────
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
───────────────────────────────────────────
Nhập lựa chọn của bạn (1-4): 7

Lựa chọn không hợp lệ, vui lòng nhập lại!

──────── HỆ THỐNG XỬ LÝ THÀNH VIÊN ────────
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
───────────────────────────────────────────
Nhập lựa chọn của bạn (1-4): 4

Chương trình đã đóng!
```
