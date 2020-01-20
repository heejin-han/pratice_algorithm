def print_grade(midterm, final):
    total = midterm + final
    if 90 <= total:
        return print("You get an A")
    elif 80<= total:
        return print("You get an B")
    elif 70<= total:
        return print("You get an C")
    elif 60<= total:
        return print("You get an D")
    elif 60> total:
        return print("You fail")
        
        
    # 코드를 쓰세요.

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)