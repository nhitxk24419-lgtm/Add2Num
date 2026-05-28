# Add2Num – Big Number Adder

| Field         | Value                       |
|---------------|-----------------------------|
| **Project**   | Add 2 Numbers               |
| **Version**   | 0.0.1                       |
| **Language**   | Python 3.10+               |
| **Create Date**| 2017-10-01                 |
| **Creator**   | Nhi.Tran                    |
| **Update Date**| 2026-03-11                 |
| **Updater**   | Nhi.Tran                   |

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

```bash
# Ví dụ: dự án trên GitHub tại https://github.com/youraccount/Add2Num
# Trên macOS/Linux:
mkdir -p ~/Projects/github.com/youraccount
cd ~/Projects/github.com/youraccount
git clone https://github.com/youraccount/Add2Num.git
cd Add2Num
```

### 2. Chạy demo

```bash
python3 main.py
```

Kết quả mẫu:

```
=============================================
  Add2Num – Big Number Adder (Python demo)
=============================================
                    1234  +  897                     =  2131
                       0  +  0                       =  0
                    9999  +  9999                    =  19998
    99999999999999999999  +  1                       =  100000000000000000000
=============================================
```

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

### 4. Chạy Benchmark

```bash
python3 benchmark.py
```

## Thuật toán

Ví dụ: `sum("1234", "897")`

```
     1 2 3 4
   +   8 9 7
   ---------
```

| Bước | digit1 | digit2 | carry_in | Tổng | digit_out | carry_out | Kết quả |
|------|--------|--------|----------|------|-----------|-----------|---------|
| 1    | 4      | 7      | 0        | 11   | 1         | 1         | "1"     |
| 2    | 3      | 9      | 1        | 13   | 3         | 1         | "31"    |
| 3    | 2      | 8      | 1        | 11   | 1         | 1         | "131"   |
| 4    | 1      | 0      | 1        | 2    | 2         | 0         | "2131"  |

**Kết quả**: `"2131"` ✅

### Cách tiếp cận

Tạo sẵn mảng kết quả có kích thước `max(len1, len2) + 1`, sau đó điền từng chữ số từ phải sang trái vào đúng vị trí. Cuối cùng `join` mảng lại thành chuỗi.

```python
result = ['0'] * max_len
# Điền từ phải sang trái
result[k] = str(digit_out)    # k giảm dần
```

## Logging

Chương trình sử dụng module `logging` chuẩn của Python để ghi nhận lịch sử phép toán:

- **INFO**: Ghi nhận lời gọi hàm và kết quả cuối cùng
- **DEBUG**: Ghi nhận chi tiết từng bước cộng (digit1, digit2, carry, total, ...)

## Phiên bản

- **0.0.1**: Phiên bản hoàn thành đầu tiên (dùng tag `v0.0.1` trên Git)
