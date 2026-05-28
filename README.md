# Add2Num

Cộng 2 số nguyên lớn biểu diễn dưới dạng chuỗi.

## Yêu cầu

- Python 3.10+
- pytest (để chạy test)

```bash
pip install pytest
```

## Cách chạy

### Chạy demo

```bash
python3 main.py
```

### Chạy Unit Test

```bash
python3 -m pytest test_my_big_number.py -v
```

## Cách sử dụng

```python
from MyBigNumber import MyBigNumber

calc = MyBigNumber()
result = calc.sum("1234", "897")
print(result)  # 2131
```
