# Bài 4 - [Phân tích] Hệ thống quản lý và chuẩn hóa dữ liệu nhân sự

## Đề bài

Phòng HR của Rikkei Education nhận dữ liệu nhân sự từ hệ thống CRM cũ. Dữ liệu đang ở dạng một chuỗi dài, còn nhiều lỗi: thừa khoảng trắng; sai định dạng viết hoa / viết thường; số điện thoại chứa dấu `-` hoặc ký tự chữ.

```python
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
```

Cần xây dựng chương trình console có menu để HR xem dữ liệu gốc, chuẩn hóa dữ liệu và tìm kiếm nhân viên theo mã ID:

```
===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
```

- **Chức năng 1:** in ra toàn bộ chuỗi `raw_data`.
- **Chức năng 2:** tách từng nhân viên, tách từng trường thông tin; chuẩn hóa **ID** viết hoa toàn bộ, **Họ tên** viết hoa chữ cái đầu mỗi từ, **Phòng ban** viết hoa toàn bộ, **Số điện thoại** xóa dấu `-`, nếu chỉ gồm chữ số thì che 6 số đầu bằng `******`, nếu có ký tự không phải số thì hiển thị `Invalid Format`; in báo cáo dạng bảng, căn lề bằng f-string.
- **Chức năng 3:** nhập mã nhân viên cần tìm (VD: `emp-002`); hệ thống xóa khoảng trắng thừa, chuyển mã tìm kiếm thành chữ hoa, so sánh với ID đã chuẩn hóa. Tìm thấy thì in thông tin nhân viên, không tìm thấy thì in `Không tìm thấy nhân viên`.
- **Chức năng 4:** in `Thoát chương trình` và dừng chương trình.

**Edge cases:**
- **Bẫy 1 - Số điện thoại sai định dạng:** chứa dấu `-` thì xóa trước khi kiểm tra; sau xử lý không hoàn toàn là chữ số thì hiển thị `Invalid Format`; hợp lệ thì che 6 số đầu.
- **Bẫy 2 - Nhập sai format khi tìm kiếm:** nhập dư khoảng trắng hoặc chữ thường vẫn phải tìm được nhân viên.
- **Bẫy 3 - Nhập sai lựa chọn menu:** ngoài phạm vi 1-4 hoặc nhập chữ thì hiển thị `Lựa chọn không hợp lệ, vui lòng nhập lại!` và tiếp tục hiển thị menu.

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Kiểu | Đặc điểm |
|---|---|---|
| `raw_data` | `str` | Nhân viên ngăn cách bởi `|`; các trường của một nhân viên ngăn cách bởi `;` theo thứ tự **ID ; Họ tên ; Số điện thoại ; Phòng ban** |
| `choice` | `str` | Lựa chọn menu |
| `search_id` | `str` | Mã nhân viên cần tìm |

| Trường | Dữ liệu thô | Xử lý | Kết quả |
|---|---|---|---|
| ID | `" eMP-001"` | `.strip().upper()` | `EMP-001` |
| Họ tên | `" nguyen van a "` | `" ".join(s.split()).title()` | `Nguyen Van A` |
| Số điện thoại | `" 0912-345-678 "` | `.strip().replace("-", "")` → `.isdigit()` → `"******" + phone[6:]` | `******5678` |
| Số điện thoại | `" 0988abc123 "` | `.isdigit()` là `False` | `Invalid Format` |
| Phòng ban | `" mkt"` | `.strip().upper()` | `MKT` |

### Đề xuất giải pháp

- **Tách 2 cấp:** `raw_data.split("|")` để được từng nhân viên; với mỗi nhân viên, `record.split(";")` để được 4 trường.
- **Chuẩn hóa ngay khi duyệt**, dùng chung cho Chức năng 2 (in bảng) và Chức năng 3 (so sánh ID).
- **Che số điện thoại** bằng slicing: giữ phần từ chỉ số 6 trở đi `phone[6:]` và nối với `"******"`.
- **Tìm kiếm:** chuẩn hóa mã nhập vào giống hệt cách chuẩn hóa ID (`strip().upper()`), so sánh `==`; dùng biến cờ `is_found` và `break` khi đã tìm thấy.
- **Menu:** `while True`; lựa chọn giữ dạng chuỗi nên nhập chữ cũng không crash (Bẫy 3).

### Thiết kế thuật toán (Pseudocode)

```
LẶP MÃI:
    IN menu; NHẬP choice (bỏ khoảng trắng)
    NẾU choice == "1": IN raw_data
    NGƯỢC LẠI NẾU choice == "2" HOẶC "3":
        NẾU "3": NHẬP search_id → strip().upper(); is_found ← False
        NẾU "2": IN tiêu đề bảng
        VỚI MỖI record TRONG raw_data.split("|"):
            fields ← record.split(";")
            id ← fields[0].strip().upper()
            name ← chuẩn hóa khoảng trắng + title(fields[1])
            phone ← fields[2].strip().replace("-", "")
            dept ← fields[3].strip().upper()
            NẾU phone toàn chữ số: phone_hien_thi ← "******" + phone[6:]
            NGƯỢC LẠI: phone_hien_thi ← "Invalid Format"
            NẾU "2": IN một dòng bảng (căn lề f-string)
            NẾU "3" VÀ id == search_id: IN thông tin; is_found ← True; DỪNG duyệt
        NẾU "3" VÀ không tìm thấy: IN "Không tìm thấy nhân viên"
    NGƯỢC LẠI NẾU choice == "4": IN "Thoát chương trình"; THOÁT
    NGƯỢC LẠI: IN "Lựa chọn không hợp lệ, vui lòng nhập lại!"
```

## (2) Triển khai code

File: [`quan_ly_nhan_su.py`](quan_ly_nhan_su.py)

```python
"""Hệ thống quản lý và chuẩn hóa dữ liệu nhân sự - Rikkei Education."""

# =====================================================================
# KHỞI TẠO: chuỗi dữ liệu thô từ hệ thống CRM cũ
# Nhân viên ngăn cách bởi "|", các trường ngăn cách bởi ";"
# =====================================================================
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
line_width = 64

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn (1-4): ").strip()

    # ----------------- Chức năng 1 -----------------
    if choice == "1":
        print("\nChuỗi dữ liệu gốc:")
        print(raw_data)

    # ----------------- Chức năng 2 và 3: cùng cần chuẩn hóa từng nhân viên -----------------
    elif choice == "2" or choice == "3":
        if choice == "3":
            # Bẫy 2: xóa khoảng trắng thừa + chuyển chữ hoa trước khi so sánh
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
            is_found = False
        else:
            print("\n" + "=" * line_width)
            print(f"{'ID':<10}{'HỌ TÊN':<20}{'SỐ ĐIỆN THOẠI':<20}{'PHÒNG BAN':<10}")
            print("-" * line_width)

        # Tách từng nhân viên theo "|"
        for employee_record in raw_data.split("|"):
            fields = employee_record.split(";")

            # Tách từng trường + chuẩn hóa
            employee_id = fields[0].strip().upper()                 # ID: viết hoa toàn bộ
            full_name = " ".join(fields[1].split()).title()         # Họ tên: viết hoa chữ cái đầu
            phone = fields[2].strip().replace("-", "")              # SĐT: xóa dấu "-"
            department = fields[3].strip().upper()                  # Phòng ban: viết hoa toàn bộ

            # Bẫy 1: số điện thoại sai định dạng
            if phone.isdigit():
                masked_phone = "******" + phone[6:]                 # che 6 số đầu
            else:
                masked_phone = "Invalid Format"

            if choice == "2":
                print(f"{employee_id:<10}{full_name:<20}{masked_phone:<20}{department:<10}")
            elif employee_id == search_id:
                print("\n[KẾT QUẢ TÌM KIẾM]")
                print(f"- ID         : {employee_id}")
                print(f"- Họ tên     : {full_name}")
                print(f"- Điện thoại : {masked_phone}")
                print(f"- Phòng ban  : {department}")
                is_found = True
                break   # đã tìm thấy -> dừng duyệt

        if choice == "2":
            print("=" * line_width)
        elif not is_found:
            print("Không tìm thấy nhân viên")

    # ----------------- Chức năng 4 -----------------
    elif choice == "4":
        print("Thoát chương trình")
        break

    # ----------------- Bẫy 3: sai lựa chọn menu -----------------
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
```

## Kết quả

Menu và Chức năng 1:

```
===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
Nhập lựa chọn (1-4): 1
```

Chức năng 2, Chức năng 3 (tìm thấy với dữ liệu nhập lộn xộn, không tìm thấy), Bẫy 3 và Thoát *(ẩn menu lặp lại cho gọn)*:

```
Chuỗi dữ liệu gốc:
 eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT 

Nhập lựa chọn (1-4): 2

================================================================
ID        HỌ TÊN              SỐ ĐIỆN THOẠI       PHÒNG BAN 
----------------------------------------------------------------
EMP-001   Nguyen Van A        ******4321          SALE      
EMP-002   Tran Thi B          ******5678          MKT       
EMP-003   Le Van C            Invalid Format      IT        
================================================================

Nhập lựa chọn (1-4): 3
Nhập mã nhân viên cần tìm:   emp-002 

[KẾT QUẢ TÌM KIẾM]
- ID         : EMP-002
- Họ tên     : Tran Thi B
- Điện thoại : ******5678
- Phòng ban  : MKT

Nhập lựa chọn (1-4): 3
Nhập mã nhân viên cần tìm: EMP-999
Không tìm thấy nhân viên

Nhập lựa chọn (1-4): 0
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-4): abc
Lựa chọn không hợp lệ, vui lòng nhập lại!

Nhập lựa chọn (1-4): 4
Thoát chương trình
```

| Kịch bản | Dữ liệu | Kết quả |
|---|---|---|
| SĐT hợp lệ | `0987654321` | `******4321` |
| SĐT có dấu `-` (Bẫy 1) | `0912-345-678` | Xóa `-` → `******5678` |
| SĐT có chữ (Bẫy 1) | `0988abc123` | `Invalid Format` |
| Tìm kiếm sai format (Bẫy 2) | `"  emp-002 "` | Tìm thấy `EMP-002` |
| Tìm không có | `EMP-999` | `Không tìm thấy nhân viên` |
| Menu sai (Bẫy 3) | `0`, `abc` | `Lựa chọn không hợp lệ, vui lòng nhập lại!` |
