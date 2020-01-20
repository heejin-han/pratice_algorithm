def calculate_change(payment,cost):
    change = payment - cost
    
    a1=change//50000
    a2=change%50000

    b1=a2//10000
    b2=a2%10000

    c1=b2//5000
    c2=b2%5000

    d1=c2//1000
    d2=c2%1000


    print("50000원 지폐: %d장" %(a1))
    print("10000원 지폐: %d장" %(b1))
    print("5000원 지폐: %d장" %(c1))
    print("1000원 지폐: %d장" %(d1))

calculate_change(100000,33000)
print()
calculate_change(500000,378000)