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
