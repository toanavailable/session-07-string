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
