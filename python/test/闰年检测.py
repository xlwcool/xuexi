# -*- coding: utf-8 -*-
"""
闰年检测程序
提供交互式界面判断年份是否为闰年，并包含自动化测试模块。
"""

import sys


def is_leap_year(year: int) -> bool:
    """
    判断指定的年份是否为闰年。

    闰年判定规则（格里高利历）：
    1. 能被4整除但不能被100整除；
    2. 或者能被400整除。

    参数:
        year (int): 待检测的年份（支持负数表示公元前）

    返回:
        bool: 如果是闰年返回 True，否则返回 False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def test_is_leap_year():
    """自动化测试模块，验证 is_leap_year 函数在各种边界条件下的正确性"""
    print("开始运行单元测试...")
    test_cases = [
        (2000, True),   # 世纪年，能被400整除 -> 闰年
        (1900, False),  # 世纪年，不能被400整除 -> 平年
        (2020, True),   # 普通非世纪年，能被4整除 -> 闰年
        (2021, False),  # 普通非世纪年，不能被4整除 -> 平年
        (4, True),      # 早期年份，能被4整除 -> 闰年
        (0, True),      # 天文学中的公元前1年 -> 闰年
        (-4, True),     # 天文学中的公元前5年 -> 闰年
        (-100, False),  # 天文学中的公元前101年 -> 平年
    ]

    passed_count = 0
    for year, expected in test_cases:
        result = is_leap_year(year)
        try:
            assert result == expected
            passed_count += 1
        except AssertionError:
            print(f"[FAIL] 测试未通过：年份 {year} 预期为 {'闰年' if expected else '平年'}，但返回为 {'闰年' if result else '平年'}")
            return

    print(f"[PASS] 所有测试通过！共成功执行 {passed_count} 个测试用例。")


def main():
    """程序主循环，处理用户输入并进行闰年判断"""
    print("==============================================")
    print("                闰年检测工具                  ")
    print(" 提示:")
    print("   1. 输入年份数字进行检测（支持负数表示公元前）")
    print("   2. 输入 'q' 或 'quit' 退出程序")
    print("   3. 输入 '--test' 运行自动化单元测试")
    print("==============================================")

    while True:
        try:
            user_input = input("\n请输入年份：").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n检测到退出信号，程序已安全退出。")
            break

        # 处理退出命令
        if user_input.lower() in ("q", "quit"):
            print("程序已退出。感谢使用！")
            break

        # 处理测试命令
        if user_input == "--test":
            test_is_leap_year()
            continue

        if not user_input:
            print("【提示】输入不能为空，请输入年份。")
            continue

        # 尝试转换为整数
        try:
            year = int(user_input)
        except ValueError:
            print("【输入错误】请输入一个有效的整数年份（例如：2024 或 -4）。")
            continue

        # 格式化输出
        is_leap = is_leap_year(year)
        if year < 0:
            year_str = f"公元前 {-year} 年 ({year}年)"
        elif year == 0:
            year_str = "公元前 1 年 (0年)"
        else:
            year_str = f"公元 {year} 年"

        if is_leap:
            print(f"[闰年] {year_str} 是 闰年。")
        else:
            print(f"[平年] {year_str} 是 平年。")


if __name__ == "__main__":
    # 支持通过命令行参数直接运行单元测试，例如: python test.py --test
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_is_leap_year()
    else:
        main()


