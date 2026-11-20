# Bài 6 - [Sáng tạo] Hệ thống quản lý & giải mã dữ liệu kho hàng

## Đề bài

Tại chuỗi cửa hàng thiết bị công nghệ Rikkei Store (thuộc Rikkei Education), mỗi khi nhập lô hàng mới, máy quét mã vạch (barcode scanner) sẽ xuất ra một chuỗi dữ liệu thô chứa thông tin toàn bộ sản phẩm. Hệ thống máy quét cũ thường xuyên trả ra chuỗi bị lỗi định dạng: dư thừa khoảng trắng, chữ hoa chữ thường lẫn lộn, đôi khi mã Serial bị sai (chứa chữ cái thay vì số).

- Mỗi mã sản phẩm chuẩn có cấu trúc 4 phần ngăn cách bởi dấu gạch ngang `-`: **[Mã Loại SP]-[Mã Quốc Gia]-[Năm Sản Xuất]-[Số Serial]** (VD: `LAP-VN-24-001`: Laptop, xuất xứ Việt Nam, năm 2024, serial 001).
- Thủ kho đang phải căng mắt dò từng mã để lọc sản phẩm lỗi Serial. Cần xây dựng module **"Hệ thống giải mã dữ liệu kho"** chạy trên CLI để tự động hóa quy trình kiểm lỗi.

**Nguồn dữ liệu lô hàng** (khai báo sẵn trong mã nguồn, các sản phẩm ngăn cách bởi `;`):

```python
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOU-vn-24-099 "
```

**Menu:**

```
===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====
1. Hiển thị chuỗi mã vạch gốc
2. Giải mã, làm sạch và in báo cáo kiểm kê
3. Tra cứu nhanh theo đuôi Serial
4. Thoát chương trình
```

- **Chức năng 1:** in trực tiếp chuỗi `raw_batch` để thủ kho đối chiếu với dữ liệu từ máy quét.
- **Chức năng 2:** tách từng mã sản phẩm bằng dấu `;`; xóa khoảng trắng thừa và chuyển toàn bộ mã về chữ hoa; tách mỗi mã thành 4 phần; chuyển năm sản xuất từ dạng `23` thành `2023`; in báo cáo dạng bảng bằng f-string gồm các cột `MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI`; cuối báo cáo hiển thị tổng kết `Đã giải mã thành công X sản phẩm hợp lệ / Tổng số Y sản phẩm.`
- **Chức năng 3:** người dùng nhập 2 số cuối của Serial cần tìm; hệ thống đối chiếu với 2 ký tự cuối của Serial trong từng mã sản phẩm; tìm thấy thì in thông tin sản phẩm, không tìm thấy thì thông báo không tìm thấy sản phẩm phù hợp.
- **Chức năng 4:** hiển thị `Đóng ca kiểm kho. Chào tạm biệt!` và kết thúc chương trình.

**Edge cases:**
- **Bẫy 1 - Serial sai định dạng:** Serial là 3 ký tự cuối của mã sản phẩm. Nếu chỉ gồm chữ số thì trạng thái **Pass**; nếu chứa chữ cái thì **Lỗi Serial - Reject** và không tính vào số sản phẩm hợp lệ (VD: `KEY-vn-23-abc` → Lỗi Serial - Reject; `LAP-VN-23-001` → Pass).
- **Bẫy 2 - Nhập dư khoảng trắng khi tra cứu:** VD `" 45 "` → `"45"`, sau đó mới so sánh với 2 ký tự cuối của serial.
- **Bẫy 3 - Nhập sai lựa chọn menu:** ngoài phạm vi 1-4 hoặc nhập chữ thì hiển thị `Chức năng không tồn tại, vui lòng nhập số từ 1-4!` và tiếp tục hiển thị menu.

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Ghi chú |
|---|---|---|---|
| Lô hàng thô | `raw_batch` | `str` | Sản phẩm ngăn cách bởi `;` |
| Mã sản phẩm đã làm sạch | `product_code` | `str` | `raw_code.strip().upper()` |
| 4 phần của mã | `product_type`, `country`, `year`, `serial` | `str` | `product_code.split("-")` |
| Năm sản xuất đầy đủ | `full_year` | `str` | `"20" + year` → `"2023"` |
| Trạng thái | `status` | `str` | `Pass` nếu `serial.isdigit()`, ngược lại `Lỗi Serial - Reject` |
| Bộ đếm | `valid_count`, `total_count` | `int` | Khởi tạo 0 trước vòng lặp, đếm khi duyệt |
| Đuôi serial cần tìm | `search_suffix` | `str` | `strip().upper()` |

**Output:** bảng kiểm kê 5 cột căn lề bằng f-string + dòng tổng kết; kết quả tra cứu; các thông báo menu.

### Đề xuất giải pháp

| Yêu cầu | Kỹ thuật chuỗi |
|---|---|
| Tách sản phẩm | `raw_batch.split(";")` |
| Làm sạch mã | `strip()` + `upper()` (`" mou-us-24-012 "` → `"MOU-US-24-012"`) |
| Tách 4 phần | `split("-")` + gán nhiều biến cùng lúc: `product_type, country, year, serial = ...` |
| Năm đầy đủ | Nối chuỗi `"20" + year` |
| Kiểm tra Serial (Bẫy 1) | `serial.isdigit()` |
| Bảng báo cáo | f-string căn trái `{product_code:<16}`, `{country:<9}`… |
| Tra cứu (Bẫy 2) | `input().strip().upper()`; so sánh với **slicing** `serial[-2:]` |
| Menu (Bẫy 3) | `while True` + `if / elif / else`; lựa chọn giữ dạng chuỗi nên gõ chữ không crash |

Tra cứu duyệt **toàn bộ** lô hàng (không `break`) vì có thể có nhiều sản phẩm cùng đuôi serial; biến cờ `is_found` để in thông báo khi không có kết quả. Mã tìm kiếm được `upper()` để gõ `bc` vẫn khớp với serial `ABC` sau chuẩn hóa.

### Thiết kế thuật toán (Pseudocode)

```
LẶP MÃI:
    IN menu; NHẬP choice
    NẾU choice == "1": IN raw_batch
    NGƯỢC LẠI NẾU choice == "2":
        valid_count ← 0; total_count ← 0
        IN tiêu đề bảng
        VỚI MỖI raw_code TRONG raw_batch.split(";"):
            product_code ← upper(strip(raw_code))
            product_type, country, year, serial ← product_code.split("-")
            full_year ← "20" + year; total_count += 1
            NẾU serial toàn chữ số: status ← "Pass"; valid_count += 1
            NGƯỢC LẠI: status ← "Lỗi Serial - Reject"
            IN một dòng bảng
        IN "Đã giải mã thành công <valid_count> sản phẩm hợp lệ / Tổng số <total_count> sản phẩm."
    NGƯỢC LẠI NẾU choice == "3":
        NHẬP search_suffix → strip().upper(); is_found ← False
        VỚI MỖI mã sản phẩm: NẾU 2 ký tự cuối của serial == search_suffix: IN sản phẩm; is_found ← True
        NẾU không tìm thấy: IN "Không tìm thấy sản phẩm phù hợp"
    NGƯỢC LẠI NẾU choice == "4": IN "Đóng ca kiểm kho. Chào tạm biệt!"; THOÁT
    NGƯỢC LẠI: IN "Chức năng không tồn tại, vui lòng nhập số từ 1-4!"
```

## (2) Triển khai code

File: [`giai_ma_kho_hang.py`](giai_ma_kho_hang.py)

```python
"""[Sáng tạo] Hệ thống quản lý & giải mã dữ liệu kho hàng - Rikkei Store."""

# =====================================================================
# KHỞI TẠO: nguồn dữ liệu lô hàng (các sản phẩm ngăn cách bởi ";")
# Cấu trúc mã chuẩn: [Mã Loại SP]-[Mã Quốc Gia]-[Năm Sản Xuất]-[Số Serial]
# =====================================================================
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOU-vn-24-099 "
line_width = 64

while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    # ----------------- Chức năng 1 -----------------
    if choice == "1":
        print("\nChuỗi mã vạch gốc từ máy quét:")
        print(f"'{raw_batch}'")

    # ----------------- Chức năng 2: giải mã + báo cáo kiểm kê -----------------
    elif choice == "2":
        valid_count = 0
        total_count = 0

        print("\n" + "=" * line_width)
        print(f"{'MÃ SP':<16}| {'XUẤT XỨ':<9}| {'NĂM SX':<8}| {'SERIAL':<8}| TRẠNG THÁI")
        print("-" * line_width)

        for raw_code in raw_batch.split(";"):
            product_code = raw_code.strip().upper()      # làm sạch + chuẩn hóa chữ hoa
            product_type, country, year, serial = product_code.split("-")
            full_year = "20" + year                       # "23" -> "2023"
            total_count += 1

            # Bẫy 1: Serial phải gồm toàn chữ số
            if serial.isdigit():
                status = "Pass"
                valid_count += 1
            else:
                status = "Lỗi Serial - Reject"

            print(f"{product_code:<16}| {country:<9}| {full_year:<8}| {serial:<8}| {status}")

        print("=" * line_width)
        print(f"Đã giải mã thành công {valid_count} sản phẩm hợp lệ / Tổng số {total_count} sản phẩm.")

    # ----------------- Chức năng 3: tra cứu theo 2 ký tự cuối của Serial -----------------
    elif choice == "3":
        # Bẫy 2: xóa khoảng trắng thừa trước khi tìm; upper() để "bc" vẫn khớp serial "ABC"
        search_suffix = input("Nhập 2 ký tự cuối của Serial cần tìm: ").strip().upper()
        is_found = False

        for raw_code in raw_batch.split(";"):
            product_code = raw_code.strip().upper()
            serial = product_code.split("-")[3]
            if serial[-2:] == search_suffix:
                status = "Pass" if serial.isdigit() else "Lỗi Serial - Reject"
                print(f"=> Tìm thấy: {product_code} (Serial {serial}, trạng thái: {status})")
                is_found = True

        if not is_found:
            print("=> Không tìm thấy sản phẩm phù hợp")

    # ----------------- Chức năng 4 -----------------
    elif choice == "4":
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break

    # ----------------- Bẫy 3: sai lựa chọn menu -----------------
    else:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
```

## Kết quả

Menu và Chức năng 1:

```
===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====
1. Hiển thị chuỗi mã vạch gốc
2. Giải mã, làm sạch và in báo cáo kiểm kê
3. Tra cứu nhanh theo đuôi Serial
4. Thoát chương trình
Nhập lựa chọn của bạn (1-4): 1
```

Chức năng 2, Chức năng 3 (dư khoảng trắng, chữ thường, không có kết quả), Bẫy 3 và Thoát *(ẩn menu lặp lại cho gọn)*:

```
Chuỗi mã vạch gốc từ máy quét:
' LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOU-vn-24-099 '

Nhập lựa chọn của bạn (1-4): 2

================================================================
MÃ SP           | XUẤT XỨ  | NĂM SX  | SERIAL  | TRẠNG THÁI
----------------------------------------------------------------
LAP-VN-23-001   | VN       | 2023    | 001     | Pass
MOU-US-24-012   | US       | 2024    | 012     | Pass
KEY-VN-23-ABC   | VN       | 2023    | ABC     | Lỗi Serial - Reject
LAP-JP-22-045   | JP       | 2022    | 045     | Pass
MOU-VN-24-099   | VN       | 2024    | 099     | Pass
================================================================
Đã giải mã thành công 4 sản phẩm hợp lệ / Tổng số 5 sản phẩm.

Nhập lựa chọn của bạn (1-4): 3
Nhập 2 ký tự cuối của Serial cần tìm:   45  
=> Tìm thấy: LAP-JP-22-045 (Serial 045, trạng thái: Pass)

Nhập lựa chọn của bạn (1-4): 3
Nhập 2 ký tự cuối của Serial cần tìm: bc
=> Tìm thấy: KEY-VN-23-ABC (Serial ABC, trạng thái: Lỗi Serial - Reject)

Nhập lựa chọn của bạn (1-4): 3
Nhập 2 ký tự cuối của Serial cần tìm: 77
=> Không tìm thấy sản phẩm phù hợp

Nhập lựa chọn của bạn (1-4): 5
Chức năng không tồn tại, vui lòng nhập số từ 1-4!

Nhập lựa chọn của bạn (1-4): abc
Chức năng không tồn tại, vui lòng nhập số từ 1-4!

Nhập lựa chọn của bạn (1-4): 4
Đóng ca kiểm kho. Chào tạm biệt!
```

| Kịch bản | Dữ liệu | Kết quả |
|---|---|---|
| Serial hợp lệ | `LAP-VN-23-001` | Pass |
| Serial có chữ (Bẫy 1) | `KEY-vn-23-abc` | Lỗi Serial - Reject, không tính vào số hợp lệ |
| Tổng kết | 5 mã | `Đã giải mã thành công 4 sản phẩm hợp lệ / Tổng số 5 sản phẩm.` |
| Tra cứu dư khoảng trắng (Bẫy 2) | `"  45  "` | Tìm thấy `LAP-JP-22-045` |
| Tra cứu chữ thường | `bc` | Tìm thấy `KEY-VN-23-ABC` (trạng thái Reject) |
| Tra cứu không có | `77` | Không tìm thấy sản phẩm phù hợp |
| Menu sai (Bẫy 3) | `5`, `abc` | `Chức năng không tồn tại, vui lòng nhập số từ 1-4!` |
