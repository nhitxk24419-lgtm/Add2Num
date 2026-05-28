"""
Demo console app – shows how to call MyBigNumber.sum().
"""

from my_big_number import MyBigNumber


def main():
    calc = MyBigNumber()

    examples = [
        ("1234", "897"),
        ("0", "0"),
        ("9999", "9999"),
        ("99999999999999999999", "1"),
    ]

    print("=" * 45)
    print("  Add2Num – Big Number Adder (Python demo)")
    print("=" * 45)
    for a, b in examples:
        result = calc.sum(a, b)
        print(f"  {a:>22}  +  {b:<22}  =  {result}")
    print("=" * 45)


if __name__ == "__main__":
    main()
