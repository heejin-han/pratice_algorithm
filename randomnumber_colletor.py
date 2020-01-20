from random import randint

chance =4
count=1

ansure =int(randint(1,20))

while chance>0 :
    num = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞취보세요: " % chance))
    if ansure>num:
        print("up")
    elif ansure<num:
        print("down")
    elif ansure == num:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % count)
        break
    chance-=1
    count+=1

if chance==0:
    print("아쉽습니다. 정답은 %d였습니다." % ansure)