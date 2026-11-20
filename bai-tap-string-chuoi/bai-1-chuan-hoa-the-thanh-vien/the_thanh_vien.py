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
