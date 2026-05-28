# Add2Num – Big Number Adder

| Field          | Value                       |
|--------------- |-----------------------------|
| **Project**    | Add 2 Numbers               |
| **Version**    | 0.0.1                       |
| **Language**   | Python 3.10+                |
| **Create Date**| 2017-10-01                  |
| **Creator**    | Nhi.Tran                    |
| **Update Date**| 2026-03-11                  | 
| **Updater**    | Nhi.Tran                    |

## Mô tả

Hàm cộng 2 số nguyên lớn (biểu diễn dưới dạng chuỗi) bằng thuật toán cộng từng chữ số từ phải sang trái giống cách học sinh Tiểu học thực hiện.

## Cấu trúc dự án

```
Add2Num/
├── my_big_number.py        # Lớp MyBigNumber – phần lõi (core)
├── main.py                 # Ứng dụng demo console
├── test_my_big_number.py   # Unit tests (14 test cases)
├── conftest.py             # Cấu hình pytest
└── README.md               # Hướng dẫn 
```

## Yêu cầu hệ thống

- **Python** 3.10 trở lên
- **pytest** (để chạy Unit Testing)

Cài pytest nếu chưa có:

```bash
pip install pytest
```

## Cách chạy

### 1. Clone dự án
# Trên macOS/Linux:
mkdir -p ~/Projects/github.com/youraccount
cd ~/Projects/github.com/youraccount
git clone https://github.com/youraccount/Add2Num.git
cd Add2Num

### 2. Chạy demo
```bash
python3 main.py
```
Kết quả mẫu:
=============================================
  Add2Num – Big Number Adder 
=============================================
Step 1: digit1=4  digit2=8  carry_in=0  total=12  digit_out=2  carry_out=1
Step 2: digit1=3  digit2=7  carry_in=1  total=11  digit_out=1  carry_out=1
Step 3: digit1=2  digit2=6  carry_in=1  total=9   digit_out=9  carry_out=0
Step 4: digit1=1  digit2=5  carry_in=0  total=6   digit_out=6  carry_out=0

Result: 1234 + 5678 = 6912
=============================================
### 3. Chạy Unit Testing

```bash
python3 -m pytest test_my_big_number.py -v
```
Kết quả mong đợi:

```
test_my_big_number.py::TestMyBigNumber::test_all_nines PASSED
test_my_big_number.py::TestMyBigNumber::test_example_from_spec PASSED
test_my_big_number.py::TestMyBigNumber::test_first_longer PASSED
test_my_big_number.py::TestMyBigNumber::test_large_equal_numbers PASSED
test_my_big_number.py::TestMyBigNumber::test_large_numbers PASSED
test_my_big_number.py::TestMyBigNumber::test_no_leading_zeros_in_result PASSED
test_my_big_number.py::TestMyBigNumber::test_number_plus_zero PASSED
test_my_big_number.py::TestMyBigNumber::test_same_length_no_carry PASSED
test_my_big_number.py::TestMyBigNumber::test_same_length_with_carry PASSED
test_my_big_number.py::TestMyBigNumber::test_second_longer PASSED
test_my_big_number.py::TestMyBigNumber::test_single_digit_no_carry PASSED
test_my_big_number.py::TestMyBigNumber::test_single_digit_with_carry PASSED
test_my_big_number.py::TestMyBigNumber::test_zero_plus_number PASSED
test_my_big_number.py::TestMyBigNumber::test_zero_plus_zero PASSED

14 passed
```
Tạo sẵn mảng kết quả có kích thước `max(len1, len2) + 1`, sau đó điền từng chữ số từ phải sang trái vào đúng vị trí. Cuối cùng `join` mảng lại thành chuỗi.

```python
result = ['0'] * max_len
# Điền từ phải sang trái
result[k] = str(digit_out)    # k giảm dần```

## Logging

Chương trình sử dụng module `logging` chuẩn của Python để ghi nhận lịch sử phép toán:

- **INFO**: Ghi nhận lời gọi hàm và kết quả cuối cùng
- **DEBUG**: Ghi nhận chi tiết từng bước cộng (digit1, digit2, carry, total, ...)

## Phiên bản

- **0.0.1**: Phiên bản hoàn thành đầu tiên (dùng tag `v0.0.1` trên Git)
