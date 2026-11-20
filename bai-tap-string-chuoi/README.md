# Bài tập Python Session 7 - String (Chuỗi)

Tổng hợp 6 bài tập thực hành về xử lý chuỗi trong Python: `split`, `strip`, `replace`, `upper`, `lower`, `title`, slicing, `isdigit`, toán tử `in`, f-string căn lề, kết hợp vòng lặp và menu điều hướng. Bối cảnh chung là các hệ thống chuẩn hóa dữ liệu của **Rikkei Education** / **Rikkei Store**.

## Danh sách bài tập

| STT | Bài tập | Loại bài | Kiến thức trọng tâm |
|---|---|---|---|
| 1 | [Xây dựng hệ thống chuẩn hóa và tạo thẻ thành viên](bai-1-chuan-hoa-the-thanh-vien/) | Bài tập tổng hợp | `split`, `strip`, `title`, `upper`, slicing, f-string căn lề, menu `while True` |
| 2 | [Lỗi chuẩn hóa thông tin học viên](bai-2-loi-chuan-hoa-thong-tin-hoc-vien/) | Vận dụng cơ bản - sửa lỗi legacy | Tính bất biến của chuỗi: phải gán lại kết quả phương thức |
| 3 | [Lỗi xử lý mã giao dịch học phí](bai-3-loi-xu-ly-ma-giao-dich-hoc-phi/) | Vận dụng cơ bản - sửa lỗi legacy | Sai delimiter khi `split`, `strip` từng phần, định dạng tiền `{:,}` |
| 4 | [Hệ thống quản lý và chuẩn hóa dữ liệu nhân sự](bai-4-quan-ly-chuan-hoa-du-lieu-nhan-su/) | Phân tích, thiết kế & code | Tách chuỗi 2 cấp, che số điện thoại bằng slicing, tìm kiếm không phân biệt hoa/thường |
| 5 | [Hệ thống chuẩn hóa mã đăng ký khóa học](bai-5-chuan-hoa-ma-dang-ky-khoa-hoc/) | Vận dụng chuyên sâu | `split("|")`, `len`, toán tử `in`, `replace`, xử lý 4 bẫy dữ liệu |
| 6 | [Hệ thống quản lý & giải mã dữ liệu kho hàng](bai-6-giai-ma-du-lieu-kho-hang/) | Sáng tạo - thiết kế toàn bộ | Giải mã cấu trúc mã sản phẩm, `isdigit`, slicing `[-2:]`, báo cáo bảng f-string |

Mỗi thư mục bài có `README.md` riêng (đề bài, phân tích, lời giải, kết quả chạy thử) và mã nguồn Python. Hai bài sửa lỗi (bài 2, 3) có cả `script_legacy.py` (code gốc bị lỗi) và `script.py` (code đã sửa).

## Cách chạy

Yêu cầu Python 3.x. Vào thư mục bài cần chạy, ví dụ:

```bash
cd bai-1-chuan-hoa-the-thanh-vien
python the_thanh_vien.py
```
