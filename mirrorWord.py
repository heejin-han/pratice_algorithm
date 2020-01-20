def is_palindrome(word):
    num1=list(word) 
    num2=list(word) 
    for count in range(0,len(num1)//2):
        temp=num1[len(num1)-count-1]
        num1[len(num1)-count-1]=num1[count]
        num1[count]=temp

    if num1==num2:
        return True
    else:
        return False
     
    # 코드를 입력하세요.

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
