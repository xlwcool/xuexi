score = float(input("请输入成绩: "))

if score > 100 or score < 0:
    print("成绩无效")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
