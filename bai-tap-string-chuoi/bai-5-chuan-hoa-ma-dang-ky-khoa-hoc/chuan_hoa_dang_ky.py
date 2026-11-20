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
