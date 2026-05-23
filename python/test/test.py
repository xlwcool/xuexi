# 闰年检测程序代码

# 检测输入的年份是否为闰年函数
def is_leap_year(year):
    # 闰年的条件：能被4整除但不能被100整除，或者能被400整除
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# 用户输入模块，获取年份，按q退出，输入非数字提示错误
def main():
    while True:
        user_input = input("请输入一个年份（输入'q'退出）：")
        if user_input.lower() == "q":
            print("程序已退出。")
            break
        if not user_input.isdigit():
            print("输入错误，请输入一个有效的年份。")
            continue

        year = int(user_input)
        if is_leap_year(year):
            print(f"{year} 是闰年。")
        else:
            print(f"{year} 不是闰年。")


# 测试模块
def test_is_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2020) == True
    assert is_leap_year(2021) == False
    print("所有测试通过。")


# 程序入口
if __name__ == "__main__":
    main()
