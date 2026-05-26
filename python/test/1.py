# 闰年检测程序

def is_leap(year):
    """
    判断给定的年份是否为闰年。
    
    根据公历规则：
    - 能被4整除但不能被100整除的是闰年。
    - 或者能被400整除的是闰年。
    
    参数:
        year (int): 需要检测的年份。
        
    返回:
        bool: 如果是闰年返回 True，否则返回 False。
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    """
    程序主入口，处理用户输入并显示结果。
    """
    print("=" * 50)
    print("          闰年检测工具")
    print("=" * 50)
    print("规则：\n"
          "1. 能被4整除但不能被100整除的是闰年。\n"
          "2. 或者能被400整除的是闰年。")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\n请输入一个年份（输入 'q' 退出）：").strip()
            
            # 退出条件
            if user_input.lower() == 'q' or user_input.lower() == 'quit':
                print("感谢使用，程序已退出。")
                break
            
            # 验证输入
            if not user_input.isdigit():
                print("输入错误：请输入一个有效的正整数年份。")
                continue
                
            year = int(user_input)
            
            # 判断并显示结果
            if is_leap(year):
                print(f"{year} 年是 闰年。")
            else:
                print(f"{year} 年是 平年。")
                
        except KeyboardInterrupt:
            print("\n程序被中断，正在退出...")
            break
        except Exception as e:
            print(f"发生错误: {e}")

# 只有当脚本直接运行时才执行 main 函数
if __name__ == "__main__":
    main()
